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

    if (move_uploaded_file($_FILES["code"]["tmp_name"], $target_file) && move_uploaded_file($_FILES["data"]["tmp_name"], $target_file)) {
        echo "The file ". basename( $_FILES["code"]["name"]). " and ". basename( $_FILES["data"]["name"]). "has been uploaded.";
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
}
?>