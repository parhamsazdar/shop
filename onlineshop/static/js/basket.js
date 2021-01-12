$(document).ready(function () {
  var $tbody = $("#basket");
  var totalCoast = 0;
  var $badge = $('#badge')


  function createRow(inventory) {
    var name_product = inventory.items.name_product;
    var price = inventory.items.price;
    var quantity = inventory.quantity;
    totalCoast += inventory.items.price * quantity;
    var row =
      "<tr id='" +
      inventory._id +
      "'name='" +
      name_product +
      "' value='" +
      quantity +
      "'price='" +
      price +
      "'name_inventory='" +
      inventory.name_inventory +
      "'>";
    row += "<td>" + name_product + "</td>";
    row += "<td>" + new Intl.NumberFormat().format(price) + "</td>";
    row += "<td>" + quantity + "</td>";
    row +=
      "<td class='text-center'>" +
      "<a  class='delete' href=\"#\">حذف</a>" +
      "</td>";
    row += "</tr>";
    $tbody.append(row);
    deleteRow(inventory);
  }

  function deleteRow(product) {
    res = $(document.getElementById(product._id))
      .find(".delete")
      .click(function () {
        var $tr = $(this).closest("tr");
        var $totalCoast = $("#totalCoast");

        $.ajax({
          url: "/api/basket/delete",
          type: "POST",
          data: {
            _id: $tr.attr("id"),
            name_product: $tr.attr("name"),
            quantity: $tr.attr("value")
          },
          success: function (resp) {
            $tr.remove();
            $badge.html(parseInt($badge.html())-1)
            $totalCoast.attr('value',
              `${parseInt($totalCoast.attr('value')) - product.items.price * product.quantity}`
            ).html(new Intl.NumberFormat().format($totalCoast.attr('value')));
          }
        });

      });
  }



  $.get("/api/basket/list", function (resp) {
    // console.log(resp)
    resp.forEach((product) => createRow(product));
    $("#totalCoast").append(new Intl.NumberFormat().format(totalCoast));
    $("#totalCoast").attr('value',totalCoast)
    var $tr = $("#basket tr");
    // console.log($('#basket tr'))
    product = "";
    for (let i = 0; i < $tr.length; ++i) {
      product +=
        "product" +
        i +
        "=" +
        $($tr[i]).attr("name") +
        "," +
        $($tr[i]).attr("value") +
        "," +
        $($tr[i]).attr("price") +
        "," +
        $tr.attr("name_inventory") +
        "&";
    }
    $("#checkOut").click(function () {
      $href = $(this).attr("href");
      $(this).attr(
        "href",
        "/cart/approve?totalCoast=" + totalCoast + "&" + product
      );
    });
  });
});
