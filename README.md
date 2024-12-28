# Attendance System

The **Attendance System** is a Python-based project that leverages facial recognition to automate attendance management. Below are its key features:

## Features

### 1. User Information Input
- The system collects the following details from users:
  - **Name**
  - **Role** (e.g., Student, Teacher, etc.)
  - **Photo Embeddings** (facial feature vectors extracted from the user's photo)
- All user data is saved into a **Redis database** using the `save_and_retrieve_data_from_redis.ipynb` file.

### 2. Attendance Logging
- The system uses facial recognition to identify users in real-time.
- If a match is found:
  - The user's **attendance** is marked with the current **date** and **time**.
  - The attendance record is saved to the Redis database.

### 3. Storage in Redis
- **User Registration:** Stores user details and facial embeddings in Redis.
- **Attendance Records:** Logs attendance data (name, role, date, and time) for each user.

### 4. Face Embeddings with Buffalo_SC Model
- The project uses the **Buffalo_SC model** to detect facial embeddings for accurate user identification.
- **Note:** The model is not included in the repository due to its large size.
- You can download the Buffalo_SC model and add it to your project directory.
- The link to it is https://drive.google.com/file/d/19I-MZdctYKmVf3nu5Da3HS6KH5LBfdzG/view?usp=sharing
- The above model is pre-trained.
- **Note** the model must be saved in a folder named "insightface_model" and in the same directory all these files are.
- I also used the cosine similarity algorithm to identify the faces


---

