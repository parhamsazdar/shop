$(document).ready(function () {
  $tbody = $("#quantity_table");
  var $select_1 = $("#inputGroupSelect01");
  var $select_2 = $("#inputGroupSelect02");
  var $modal = $("#Modal_Edition_Quantity");

  function createRow(inventory) {
    name_inventery = inventory.name_inventory;
    if (!inventory["result"] && inventory.items) {
      name_product = inventory.items.name_product;
      price = inventory.items.price;
      quantity = inventory.items.quantity;
    } else {
      name_product = inventory.name_product;
      price = inventory.price;
      quantity = inventory.quantity;
    }

    var row =
      "<tr id='" +
      inventory._id +
      "' name_product='" +
      name_product +
      "' class='" +
      inventory._id +
      "' name='" +
      name_product +
      inventory._id +
      "'>";
    row += "<td>" + name_inventery + "</td>";
    row += "<td>" + name_product + "</td>";
    row += "<td>" + price + "</td>";
    row += "<td>" + quantity + "</td>";
    row +=
      "<td class='text-center'>" +
      '<a data-toggle="modal" href="#Modal_Edition_Quantity">ویرایش</a>' +
      "  " +
      "<a  class='delete' href=\"#\">حذف</a>" +
      "</td>";
    row += "</tr>";
    $tbody.append(row);

    deleteRow(inventory);
    handleEditLink(inventory);
  }

  function deleteRow(inventory) {
    var tr = document.getElementsByClassName(inventory._id);
    for (let i = 0; i < tr.length; ++i) {
      $(tr[i])
        .find(".delete")
        .click(function () {
          var $tr = $(this).closest("tr");
          $.ajax({
            url: "/api/inventory/delete_prod",
            type: "POST",

            data: {
              _id: $tr.prop("id"),
              name_product: $tr.attr("name_product")
            },
            success: function (resp) {
              $($tr).remove();
            }
          });
        });
    }
  }

  function handleEditLink(inventory) {
    $(document.getElementById(inventory._id))
      .find('a[href="#Modal_Edition_Quantity"]')
      .click(function () {
        $modal.prop("value", inventory._id);
        $modal.attr("name_product", inventory.items.name_product);
        console.log("kir");
      });
  }

  function setChange(inventory) {
    console.log(inventory);
    var $tds = $(
      document.getElementsByName(inventory.name_product + inventory._id)
    ).find("td");
    $($tds[2]).html(inventory.price);
    $price = $($tds[3]).text();
    $($tds[3]).html(parseInt($price) + parseInt(inventory.quantity));
  }

  function handleProductName(product, $select) {
    var $option =
      "<option value='" +
      product.name_product +
      "'>" +
      product.name_product +
      "</option>";
    $select.append($option);
  }
  function handleInventorytName(inventory, $select) {
    var $option =
      "<option value='" +
      inventory._id +
      "'>" +
      inventory.name_inventory +
      "</option>";
    $select.append($option);
  }
  function handleProductDropDwonAjax() {
    $.ajax({
      url: "/api/inventory/items",
      type: "POST",
      data: { _id: $valueModal.prop("value") },
      success: function (resp) {
        console.log(resp);
        $select_2.empty();
        $select_3.empty();
        resp.forEach((product) => handleProductName2(product));
      }
    });
  }

  $.get("/api/quantity/quantity_list", function (resp) {
    console.log(resp);
    resp.forEach((inventory) => createRow(inventory));
  });

  $.ajax({
    url: "/api/product/list",
    success: function (resp) {
      resp.forEach((product) => handleProductName(product, $select_1));
    }
  });
  $.get("/api/inventory/list", function (resp) {
    resp.forEach((inventory) => handleInventorytName(inventory, $select_2));
  });

  $("#add_button").click(function () {
    $.ajax({
      url: "/api/quantity/quantity_add",
      type: "POST",
      data: {
        _id: $select_2.prop("value"),
        name_product: $select_1.prop("value"),
        price: $("#price").val(),
        quantity: $("#num").val()
      },
      success: function (resp) {
        if (!resp["result"]) {
          console.log(!resp["result"]);
          createRow(resp);
          $("#Modal_add").modal("hide");
        } else {
          setChange(resp);
        }
      }
    });
  });

  $("#edit_button").click(function () {
    $.ajax({
      url: "/api/inventory/edit",
      data: {
        _id: $modal.prop("value"),
        name_product: $modal.attr("name_product"),
        price: $("#num_price").val(),
        quantity: $("#Modal_Edition_Quantity #num_prod").val()
      },
      type: "POST",
      success: function (resp) {
        setChange(resp[1]);
        alert(resp[0]["result"]);
        $modal.modal("hide");
      }
    });
  });
});
