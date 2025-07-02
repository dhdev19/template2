<?php
if(isset($_POST['contactbut']) && !empty($_POST))
{
require("class.phpmailer.php");
$mail2 = new PHPMailer();
//$mail2->IsSMTP();
$mail2->IsMAIL();
$mail2->Host = "chandiwalaandheriwest.com";
$mail2->SMTPAuth = true;
$mail2->Port = 587;
$mail2->Username = "info@chandiwalaandheriwest.com";
$mail2->Password = "Siddarth@123#";
$mail2->From = "info@chandiwalaandheriwest.com";
$mail2->FromName = "Chandiwala Prarambh";
$mail2->AddAddress("leads@gurukrupamarque.com");
//$mail2->AddBCC("leads@chandiwalaandheriwest.com");
//$mail->AddReplyTo("mail@mail.com");
$mail2->IsHTML(true);
$mail2->Subject = "Contact Us";

$mail2->Body = "<table><tr><td>Name</td><td>:</td><td>".$_POST['name']."</td></tr><tr><td>Phone Number</td><td>:</td><td>".$_POST['phone']."</td></tr><tr><td>IP Address:</td><td>:</td><td>".$_SERVER['REMOTE_ADDR']."</td></tr></table>";

//$mail->AltBody = "This is the body in plain text for non-HTML mail clients";
if(!$mail2->Send())
{
echo "Message could not be sent. <p>";
echo "Mailer Error: " . $mail2->ErrorInfo;
exit;
}
header("Location:thank-you.php");
}




if(isset($_POST['callback']) && !empty($_POST))
{
require("class.phpmailer.php");
$mail3 = new PHPMailer();
//$mail3->IsSMTP();
$mail3->IsMAIL();
$mail3->Host = "chandiwalaandheriwest.com";
$mail3->SMTPAuth = true;
$mail3->Port = 587;
$mail3->Username = "info@chandiwalaandheriwest.com";
$mail3->Password = "Siddarth@123#";
$mail3->From = "info@chandiwalaandheriwest.com";
$mail3->FromName = "Chandiwala Prarambh";
$mail3->AddAddress("leads@gurukrupamarque.com");
//$mail3->AddBCC("leads@chandiwalaandheriwest.com");
//$mail->AddReplyTo("mail@mail.com");
$mail3->IsHTML(true);
$mail3->Subject = "Request Callback";

$mail3->Body = "<table><tr><td>Name</td><td>:</td><td>".$_POST['name']."</td></tr><tr><td>Phone Number</td><td>:</td><td>".$_POST['phone']."</td></tr><tr><td>IP Address:</td><td>:</td><td>".$_SERVER['REMOTE_ADDR']."</td></tr></table>";

//$mail->AltBody = "This is the body in plain text for non-HTML mail clients";
if(!$mail3->Send())
{
echo "Message could not be sent. <p>";
echo "Mailer Error: " . $mail2->ErrorInfo;
exit;
}
header("Location:thank-you.php");
}





if(isset($_POST['brochure']) && !empty($_POST))
{
require("class.phpmailer.php");
$mail4 = new PHPMailer();
//$mail3->IsSMTP();
$mail4->IsMAIL();
$mail4->Host = "chandiwalaandheriwest.com";
$mail4->SMTPAuth = true;
$mail4->Port = 587;
$mail4->Username = "info@chandiwalaandheriwest.com";
$mail4->Password = "Siddarth@123#";
$mail4->From = "info@chandiwalaandheriwest.com";
$mail4->FromName = "Chandiwala Prarambh";
$mail4->AddAddress("leads@gurukrupamarque.com");
//$mail4->AddBCC("leads@chandiwalaandheriwest.com");
//$mail->AddReplyTo("mail@mail.com");
$mail4->IsHTML(true);
$mail4->Subject = "Download Brochure";

$mail4->Body = "<table><tr><td>Name</td><td>:</td><td>".$_POST['name']."</td></tr><tr><td>Phone Number</td><td>:</td><td>".$_POST['phone']."</td></tr><tr><td>IP Address:</td><td>:</td><td>".$_SERVER['REMOTE_ADDR']."</td></tr></table>";

//$mail->AltBody = "This is the body in plain text for non-HTML mail clients";
if(!$mail4->Send())
{
echo "Message could not be sent. <p>";
echo "Mailer Error: " . $mail2->ErrorInfo;
exit;
}
header("Location:thank-you-brochure.php");
}



?>