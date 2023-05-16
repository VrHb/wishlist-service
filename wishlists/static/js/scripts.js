  function reveal()
  {
  if(document.getElementById('flexSwitchCheckDefault').checked)
     {document.getElementById("id_password").type='text';}
  else
  document.getElementById("id_password").type='password';
  }

  function reveal_reg()
  {
  if(document.getElementById('flexSwitchCheckDefault').checked)
     {document.getElementById("id_password1").type='text';}
  else
  document.getElementById("id_password1").type='password';
  if(document.getElementById('flexSwitchCheckDefault').checked)
     {document.getElementById("id_password2").type='text';}
  else
  document.getElementById("id_password2").type='password';
  }
