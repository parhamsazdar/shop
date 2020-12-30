$(document).ready(function () {
  $("#box_product").empty();
  function createRow(product) {
    var send = product[0];
    $.ajax("/test2/category/list_url", {
      type: "POST",
      data: { name_product: send },
      success: function (data, status, xhr) {
        txt = "";
        txt =
          "<div class='d-flex flex-row-reverse  m-3 align-items-center justify-content-around col-lg-4 col-5 col-sm-8 col-md-5 border'>";
        txt += "<div>";
        txt += `<h5 class='text-center' id='name_product'>${product[0]}</h5>`;
        txt += `<h2 id='price_product'>${product[1]}تومان</h2>`;
        txt += "</div>";
        txt += "<div class='pr-0'>";
        txt += `<img src='${data}' alt='Img NotFound!' width='100px'>`;

        txt += "</div>";
        txt += "</div>";
        $("#box_product").append(txt);
      },
      error: function (jqXhr, textStatus, errorMessage) {
        console.log("errrrrrrr");
      },
    });
  }

  $.get("/test2/category/list", function (resp) {
    console.log(resp);
    console.log("iman masroori");
    resp.forEach((product) => createRow(product));
  });

  function category_sidbar(cat) {
    $("#list_right").empty();
    console.log("-------------------",cat)
    txt2 = '';
    txt2 += "<li class='active'>"
    txt2 += `<a class='h4'>${cat['subcategories'][0]['name']}</a>`
    txt2 += " <ul class='list-unstyled'>"
    txt2 += "<li class='h5'>"
    txt2 +=   `<a href='#'>${cat['subcategories'][1]['name']}</a>`
    txt2 +=" </li>"
    txt2 +=  "<li class='h4'>"
    txt2 +=   "<a href='#'>شیر</a>"
    txt2 += "</li>"
    txt2 += "</ul>"

    txt2 += "</li>"
    $("#list_right").append(txt2);
  }
  $.get("/api/product/json_category", function (resp) {
    console.log(resp);
    console.log("iman masroori");
    resp.forEach((cat) => category_sidbar(cat));
  });
});
