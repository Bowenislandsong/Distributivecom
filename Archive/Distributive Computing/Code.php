<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Dogedojo</title>

    <!-- Latest compiled and minified CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

  <!-- Optional theme -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css">
  <link rel="stylesheet" href="overrides.css">
    </head>
<body>

  <div class="container" id="login">
    <div class="row">
      <div class="col-lg-12 text-center">
        <img src="medusa.jpg" class="mainDoge">
        <h2>Welcome to Medusa</h2>
        <button type="button" class="btn btn-primary" onclick="signIn();"><i class="fa fa-google-plus"></i> Sign-In With Google</button>

      </div>
    </div>
   

  </div><!-- /.container -->

  <div class="container" id="welcome">
    <!-- Learn about this code on MDN: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/file -->

<form method="post" enctype="multipart/form-data" action="DC_Client.php">
  <div>
    <label for="code">Choose code file to upload</label>
    <input type="file" id="code" name="code"
          accept=".py, .java, .cpp, .c"><br>&nbsp;&nbsp;
     <label for="code">Choose data file to upload</label>
    <input type="file" id="data" name="data"
          accept=".csv, .zip">
  </div>
  <div>
  <input type="submit" value="Upload Files" name="submit">
  </div>
</form>

<?php
if(isset($_POST["submit"])) {
$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["code"]["name"]);
$target_file_data = $target_dir . basename($_FILES["data"]["name"]);
$uploadOk = 1;
$FileType = pathinfo($target_file,PATHINFO_EXTENSION);
$FileType_data = pathinfo($target_file_data,PATHINFO_EXTENSION);

// Check if image file is a actual image or fake image

    if (move_uploaded_file($_FILES["code"]["tmp_name"], $target_file) || move_uploaded_file($_FILES["data"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["code"]["name"]). " and ". basename( $_FILES["data"]["name"]). "has been uploaded.";
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
}
?>
  </div>


<!--   <script src="https://www.gstatic.com/firebasejs/4.5.2/firebase.js"></script>
  <script>
    // Initialize Firebase
    var config = {
      apiKey: "AIzaSyDYak5RSWQR2yWdJU--bZUeZXNPUJlq8aE",
      authDomain: "dclogin-ba56e.firebaseapp.com",
      databaseURL: "https://dclogin-ba56e.firebaseio.com",
      projectId: "dclogin-ba56e",
      storageBucket: "",
      messagingSenderId: "941856178063"
    };
    firebase.initializeApp(config);
  </script>
  <script src="https://apis.google.com/js/platform.js" async defer></script>  -->
  
<script src="https://www.gstatic.com/firebasejs/4.6.0/firebase.js"></script>
<script>
  // Initialize Firebase
  var config = {
    apiKey: "AIzaSyAC_TQcZx0LNaYG6lHD1DDHTb_cw5M8IEQ",
    authDomain: "distributive-computing.firebaseapp.com",
    databaseURL: "https://distributive-computing.firebaseio.com",
    projectId: "distributive-computing",
    storageBucket: "distributive-computing.appspot.com",
    messagingSenderId: "260081266013"
  };
  firebase.initializeApp(config);
</script>


  <!-- Bootstrap core JavaScript
  ================================================== -->
  <!-- Placed at the end of the document so the pages load faster -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
  <!-- Latest compiled and minified JavaScript -->
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
  <script type="text/javascript" src="myjs.js"></script>

</body>
</html>