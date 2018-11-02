function borrar(id_invernadero, nombre_invernadero){
  $('#borrarModal').modal('hide');
    url = "/ajax/borrar-invernadero/";
    $.ajax({
      url: url,
      type: 'POST',
      contentType: 'application/json',
      data: {
        'id_invernadero': id_invernadero,
        'action': 'borrar',
        'csrfmiddlewaretoken': '{{ csrf_token }}',
      },
      dataType: 'json',
      succes: function(data){
        if(data.is_done){
          alert("El invernadero "+nombre_invernadero+ " fue borrado exitosamente");
        }else{
          alert("El invernadero "+nombre_invernadero+ " no pudo ser eliminado");
        }
      }
    });
 }

function confirmarBorrado(id_invernadero, nombre_invernadero){
    $('#modalBodyBorrar').empty();
    $('#modalBodyBorrar').append(
      "<p>¿Seguro que desea eliminar el invernadero <strong>"+nombre_invernadero+"</strong>?</p>"+
      "<p>Seleccione 'Continuar' para confirmar la acción</p>"
    );
    $('#modalFooterBorrar').empty();
    $('#modalFooterBorrar').append(
      "<button class='btn btn-primary' type='button' data-dismiss='modal'>Cancelar</button>"+
      "<button id='confirmacion' class='btn btn-danger' href='#'>Continuar</button>"
    )
    $('#borrarModal').modal('show');
    $('#confirmacion').attr('onclick', 'borrar('+id_invernadero+', \''+nombre_invernadero+'\')');
  //  url = "La url como la declara DJANGo";
   // $.ajax({
  //    url: url,
 //     type: 'POST',
 //     data: {'variable': valor },
  //  })
  //  .done(function(respuesta) {

  //      })
  //      .fail(function() {
 //         console.log("error");
 //       })
 //       .always(function() {
 //         console.log("complete");
   //     });
//  } dame unos minutos me estan llamando esta bien
 }
 $(function () {
  $.ajaxSetup({
      headers: { "X-CSRFToken": getCookie("csrftoken") }
  });
});