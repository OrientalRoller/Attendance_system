# Attendance_system
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

    <p>This system ensures efficient and accurate attendance management by combining facial recognition and fast data storage with Redis.</p>
