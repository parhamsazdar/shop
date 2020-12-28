$(document).ready(function () {
  var $tbody = $("#inventory_table");
  var $select_2 = $("#inputGroupSelect01");
  var $select_1 = $("#inputGroupSelect02");
  var $select_3 = $("#inputGroupSelect03");
  var $valueModal = $("#Modal_Edition_Inventory");

  function createRow(inventory) {
    var name = inventory.name_inventory;
    var row = "<tr id='" + inventory._id + "'>";
    row += "<td>" + name + "</td>";
    row +=
      "<td class='text-center'>" +
      '<a data-toggle="modal" href="#Modal_Edition_Inventory">ویرایش</a>' +
      "  " +
      "<a  class='delete' href=\"#\">حذف</a>" +
      "</td>";
    row += "</tr>";
    $tbody.append(row);
    deleteRow(inventory);
    handleEditLink(inventory);
  }

  function deleteRow(inventory) {
    res = $(document.getElementById(inventory._id))
      .find(".delete")
      .click(function () {
        var $tr = $(this).closest("tr");
        url = "/api/inventory/delete/" + $tr.attr("id");
        $.get(url);
        $($tr).remove();
      });
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

  function handleEditLink(inventory) {
    $(document.getElementById(inventory._id))
      .find('a[href="#Modal_Edition_Inventory"]')
      .click(function () {
        $valueModal.prop("value", inventory._id);
        handleProductDropDwonAjax();
      });
  }

  function handleProductName(product) {
    var $option =
      "<option value='" +
      product.name_product +
      "'>" +
      product.name_product +
      "</option>";
    $select_1.append($option);
  }

  function handleProductName2(product) {
    var $option =
      "<option value='" +
      product.name_product +
      "'>" +
      product.name_product +
      "</option>";
    $select_2.append($option);
    $select_3.append($option);
  }

  function setChange(inventory) {
    var $tds = $(document.getElementById(inventory._id)).find("td");
    $($tds[0]).html(inventory.name_inventory);
  }

  $.ajax({
    url: "/api/product/list",
    success: function (resp) {
      resp.forEach((product) => handleProductName(product));
    }
  });

  $.get("/api/inventory/list", function (resp) {
    resp.forEach((product) => createRow(product));
  });

  $("#add_inventory").click(function () {
    $.ajax({
      url: "/api/inventory/add",
      success: function (resp) {
        console.log(resp);
        resp.forEach((inventory) => createRow(inventory));
      }
    });
  });

  $("#edit_button").click(function () {
    $.ajax({
      url: "/api/inventory/edit",
      data: {
        _id: $("#Modal_Edition_Inventory").prop("value"),
        name_product: `${$(
          "#Modal_Edition_Inventory #inputGroupSelect01"
        ).val()}`,
        price: `${$("#Modal_Edition_Inventory #num_price").val()}`,
        quantity: `${$("#Modal_Edition_Inventory #num_prod").val()}`
      },
      type: "POST",
      success: function (resp) {
        alert(resp["result"]);
        $("#Modal_Edition_Inventory").modal("hide");
      }
    });
  });

  $("#add_product").click(function () {
    $.ajax({
      url: "/api/inventory/add_prod",
      type: "POST",
      data: {
        _id: $("#Modal_Edition_Inventory").prop("value"),
        name_product: `${$(
          "#Modal_Edition_Inventory #inputGroupSelect02"
        ).val()}`,
        price: `${$("#Modal_Edition_Inventory #price_prod_add").val()}`,
        quantity: `${$("#Modal_Edition_Inventory #num_prod_add").val()}`
      },
      success: function (resp) {
        alert(resp["result"]);
        $("#Modal_Edition_Inventory").modal("hide");
        handleProductDropDwonAjax();
      }
    });
  });
  $("#edit_name").click(function () {
    $.ajax({
      url: "/api/inventory/edit_name_inventory",
      type: "POST",
      data: {
        _id: $("#Modal_Edition_Inventory").prop("value"),
        name_inventory: $("#inventory_name").prop("value")
      },
      success: function (resp) {
        resp.forEach((inventory) => setChange(inventory));
        $("#Modal_Edition_Inventory").modal("hide");
      }
    });
  });

  $("#delete_prod").click(function () {
    $.ajax({
      url: "/api/inventory/delete_prod",
      type: "POST",
      data: {
        _id: $("#Modal_Edition_Inventory").prop("value"),
        name_product: $select_3.prop("value")
      },
      success: function (resp) {
        alert(resp["result"]);
        handleProductDropDwonAjax();
      }
    });
  });
});
