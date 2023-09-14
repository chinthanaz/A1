<!DOCTYPE html>
<html>
<head>
    <title>Marks Calculator</title>
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

        form {
            max-width: 300px;
            margin: 0 auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }

        input[type="number"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }

        input[type="submit"] {
            background-color: #007BFF;
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 3px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Marks Calculator</h1>

    <form action="calculate.php" method="post">
        <label for="maths">Maths:</label>
        <input type="number" name="maths" id="maths" required>

        <label for="chemistry">Chemistry:</label>
        <input type="number" name="chemistry" id="chemistry" required>

        <label for="physics">Physics:</label>
        <input type="number" name="physics" id="physics" required>

        <input type="submit" name="calculate" value="Calculate">
    </form>
</body>
</html>
