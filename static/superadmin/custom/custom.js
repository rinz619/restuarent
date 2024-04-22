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





function filtercategory(data) {
  var page = '1'
    if(data != 'None'){
      page=data
    }


//    var search = $('#searchkey').val()
    var status = $('#status').val()

    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status},

      success: function(data) {

        $(".table-responsive").html(data.template)


      }
  });
  }



 function categorystatus(id,vl) {

      page=$("#page").val();


//    var search = $('#searchkey').val()
    var status = $('#status').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,vl:vl,type:1},

      success: function(data) {

       $(".table-responsive").html(data.template)


      }
  });
  }


 function categorydelete() {

      page=$("#page").val();
      id=$("#hid").val();


//    var search = $('#searchkey').val()
    var status = $('#status').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,type:2},

      success: function(data) {
        $("#modaldemo5").modal('hide');

       $(".table-responsive").html(data.template)


      }
  });
  }






function filtermenu(data) {
  var page = '1'
    if(data != 'None'){
      page=data
    }


//    var search = $('#searchkey').val()
    var status = $('#status').val()

    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status},

      success: function(data) {

        $(".table-responsive").html(data.template)


      }
  });
  }



 function menustatus(id,vl) {

      page=$("#page").val();


//    var search = $('#searchkey').val()
    var status = $('#status').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,vl:vl,type:1},

      success: function(data) {

       $(".table-responsive").html(data.template)


      }
  });
  }


 function menudelete() {

      page=$("#page").val();
      id=$("#hid").val();


//    var search = $('#searchkey').val()
    var status = $('#status').val()
    var url = $('#url').val()
    $.ajax({
      url: url,
      type: 'GET',
      data: {page:page,status:status,id:id,type:2},

      success: function(data) {
        $("#modaldemo5").modal('hide');

       $(".table-responsive").html(data.template)


      }
  });
  }





