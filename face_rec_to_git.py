import numpy as np
import pandas as pd
import cv2

import redis
from insightface.app import FaceAnalysis
from sklearn.metrics import pairwise
import time
from datetime import datetime


r =redis.Redis(
    host='host_id_in_redis',
    port="no_after_host_id",

    password='the_redis_db_password',
)

faceapp=FaceAnalysis(name='buffalo_sc',
                     root='insightface_model',
                     )
faceapp.prepare(ctx_id=0, det_size=(640,640),det_thresh=0.5)

#ml search algo
# def ml_search_algorithm(dataframe,feature_column,test_vector,name_role=["Name",'Role'],thresh=0.5):
#     """
#     cosine similarity base search algorithm

#     """
#     dataframe=dataframe.copy()
#     X_list=dataframe[feature_column].tolist()
#     x=np.asarray(X_list)
    
#     similar=pairwise.cosine_similarity(x,test_vector.reshape(1,512))
#     similar_arr=np.array(similar).flatten()
#     dataframe['cosine_similarity']=similar_arr
    
#     data_filter=dataframe.query(f'cosine_similarity >= {thresh}')
#     if len(data_filter)>0:
#         data_filter.reset_index(drop=True,inplace=True)
#         argmax=data_filter['cosine_similarity'].argmax()
#         person_name, person_role=data_filter.loc[argmax][name_role]
#     else:
#         person_name,person_role="unknown","unkown"
#     return person_name, person_role
def ml_search_algorithm(dataframe, feature_column, test_vector, name_role=["Name", "Role"], thresh=0.5):
    """
    Cosine similarity-based search algorithm.
    """
    # Filter valid embeddings
    dataframe = dataframe[dataframe[feature_column].apply(lambda x: isinstance(x, (list, np.ndarray)) and len(x) == 512)]
    X_list = dataframe[feature_column].tolist()
    x = np.vstack(X_list)  # Convert to a 2D array

    # Compute cosine similarity
    similar = pairwise.cosine_similarity(x, test_vector.reshape(1, 512))
    similar_arr = np.array(similar).flatten()
    dataframe['cosine_similarity'] = similar_arr

    # Filter based on threshold
    data_filter = dataframe.query(f'cosine_similarity >= {thresh}')
    if len(data_filter) > 0:
        data_filter.reset_index(drop=True, inplace=True)
        argmax = data_filter['cosine_similarity'].argmax()
        person_name, person_role = data_filter.loc[argmax][name_role]
    else:
        person_name, person_role = "unknown", "unknown"

    return person_name, person_role
# def ml_search_algorithm(dataframe, feature_column, test_vector, name_role=["Name", "Role"], thresh=0.5):
#     """
#     Cosine similarity-based search algorithm for 1024-dimensional embeddings.
#     """
#     # Filter valid embeddings of size 1024
#     dataframe = dataframe[dataframe[feature_column].apply(lambda x: isinstance(x, (list, np.ndarray)) and len(x) == 1024)]
#     X_list = dataframe[feature_column].tolist()
#     x = np.vstack(X_list)  # Convert to a 2D array

#     # Compute cosine similarity
#     similar = pairwise.cosine_similarity(x, test_vector.reshape(1, 1024))
#     similar_arr = np.array(similar).flatten()
#     dataframe['cosine_similarity'] = similar_arr

#     # Filter based on threshold
#     data_filter = dataframe.query(f'cosine_similarity >= {thresh}')
#     if len(data_filter) > 0:
#         data_filter.reset_index(drop=True, inplace=True)
#         argmax = data_filter['cosine_similarity'].argmax()
#         person_name, person_role = data_filter.loc[argmax][name_role]
#     else:
#         person_name, person_role = "unknown", "unknown"

#     return person_name, person_role
class RealTimePred:
    def __init__(self):
        self.logs=dict(name=[],role=[],current_time=[])
    def reset_dict(self):
        self.logs=dict(name=[],role=[],current_time=[])
    def saveLogs_redis(self):
        dataframe=pd.DataFrame(self.logs)
        dataframe.drop_duplicates('name', inplace=True)
        name_list=dataframe['name'].tolist()
        role_list=dataframe['role'].tolist() 
        ctime=dataframe['current_time'].tolist()
        encoded_data=[]
        for name,role,time in zip(name_list,role_list,ctime):
            if name!="Unknown":
                concat_string=f"{name}@{role}@{ctime}"
                encoded_data.append(concat_string)
                
        if len(encoded_data)>0:
            r.lpush("attendence:logs",*encoded_data)
            
        self.reset_dict()
    def face_prediction(self, test_image, dataframe,feature_column,name_role=["Name",'Role'],thresh=0.5):
        current_time=str(datetime.now())
        
        
        result=faceapp.get(test_image)
        test_copy=test_image.copy()
        for res in result:
            x1,y1,x2,y2=res['bbox'].astype(int)
            embeddings=res['embedding']
            person_name,person_role=ml_search_algorithm(dataframe,feature_column,test_vector=embeddings,name_role=name_role,thresh=thresh)
            if person_name=="unknown":
                color=(0,0,255)
            else:
                color=(0,255,0)
            cv2.rectangle(test_copy,(x1,y1),(x2,y2),color)
            
            text_gen=person_name
            cv2.putText(test_copy,text_gen,(x1,y1-10),cv2.FONT_HERSHEY_DUPLEX,1,color,2,)
            cv2.putText(test_copy, current_time, (x1,y2+10),cv2.FONT_HERSHEY_DUPLEX,1,color,2,)
            self.logs['name'].append(person_name)
            self.logs['role'].append(person_role)
            self.logs['current_time'].append(current_time)
        return test_copy
        # cv2.imshow('test_images',test_copy)
        # cv2.waitKey()
        # cv2.destroyAllWindows()