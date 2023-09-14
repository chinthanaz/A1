<!DOCTYPE html>
<html>
<head>
    <title>Marks Calculator - Results</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 0;
            padding: 0;
        }

        h1 {
            text-align: center;
            margin-top: 20px;
            color: #333;
        }

        p {
            text-align: center;
            font-weight: bold;
            font-size: 18px;
            margin-top: 10px;
            color: #333;
        }
    </style>
</head>
<body>
    <h1>Results</h1>

    <?php
    if (isset($_POST['maths']) && isset($_POST['chemistry']) && isset($_POST['physics'])) {
        $maths = $_POST['maths'];
        $chemistry = $_POST['chemistry'];
        $physics = $_POST['physics'];

        $total = $maths + $chemistry + $physics;
        $average = $total / 3;

        echo "<p>Maths: $maths</p>";
        echo "<p>Chemistry: $chemistry</p>";
        echo "<p>Physics: $physics</p>";
        echo "<p>Total Marks: $total</p>";
        echo "<p>Average Marks: $average</p>";
    } else {
        echo "<p>No data submitted. Please fill out the form.</p>";
    }
    ?>
</body>
</html>
