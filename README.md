<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Attendance System Project</title>
</head>
<body>
    <h1>Attendance System</h1>
    <p>The <strong>Attendance System</strong> is a Python-based project that leverages facial recognition to automate attendance management. Below are its key features:</p>

    <h2>1. User Information Input</h2>
    <ul>
        <li>The system collects the following details from users:
            <ul>
                <li><strong>Name</strong></li>
                <li><strong>Role</strong> (e.g., Student, Teacher, etc.)</li>
                <li><strong>Photo Embeddings</strong> (facial feature vectors extracted from the user's photo)</li>
            </ul>
        </li>
        <li>All user data is saved into a <strong>Redis database</strong> using the <code>save_and_retrieve_data_from_redis.ipynb</code> file.</li>
    </ul>

    <h2>2. Attendance Logging</h2>
    <ul>
        <li>The system uses facial recognition to identify users in real time.</li>
        <li>If a match is found:
            <ul>
                <li>The user's <strong>attendance</strong> is marked with the current <strong>date</strong> and <strong>time</strong>.</li>
                <li>The attendance record is saved to the Redis database.</li>
            </ul>
        </li>
    </ul>

    <h2>3. Storage in Redis</h2>
    <ul>
        <li><strong>User Registration:</strong> Stores user details and facial embeddings in Redis.</li>
        <li><strong>Attendance Records:</strong> Logs attendance data (name, role, date, and time) for each user.</li>
    </ul>

    <h2>4. Face Embeddings with Buffalo_SC Model</h2>
    <ul>
        <li>The project uses the <strong>Buffalo_SC model</strong> to detect facial embeddings for accurate user identification.</li>
        <li><strong>Note:</strong> The model is not included in the repository due to its large size.</li>
        <li>You can download the Buffalo_SC model and add it to your project directory.</li>
    </ul>

    <h2>How to Use</h2>
    <ol>
        <li>Clone the repository.</li>
        <li>Download the Buffalo_SC model and place it in the appropriate directory (as instructed in the code).</li>
        <li>Install the necessary dependencies using <code>pip install -r requirements.txt</code>.</li>
        <li>Run the <code>save_and_retrieve_data_from_redis.ipynb</code> notebook to register users.</li>
        <li>Run the main script to start the attendance system.</li>
    </ol>

    <p>This system ensures efficient and accurate attendance management by combining facial recognition and fast data storage with Redis.</p>
</body>
</html>
