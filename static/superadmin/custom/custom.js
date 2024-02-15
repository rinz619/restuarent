  function restrictAlphabets(e){
    argumentsl 
       var x = e.which || e.keycode;
   	if((x>=48 && x<=57))
   		return true;
   	else
   		return false;
   }

 $("#message_div").fadeOut(3000);

function delete_modal(id){
    $("#hid").val(id);
    $("#modaldemo5").modal('show');
}


function filterdata(data) {
  var page = '1'
    if(data != 'None'){
      page=data
    }



    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page},

      success: function(data) {

        $(".table-responsive").html(data.template)


      }
  });
  }



 function deletedata() {

      page=$("#page").val();
      id=$("#hid").val();

    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,id:id},

      success: function(data) {
        $("#modaldemo5").modal('hide');

       $(".table-responsive").html(data.template)


      }
  });
  }

