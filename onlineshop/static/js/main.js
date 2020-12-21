$(document).ready(function () {
    $tbody = $("#product_table")
    console.log($tbody.html())
    $.get('/api/product/list', function (resp) {
        resp.forEach(function (product) {

            var name = product.name_product;
            var category = product.category;
            var image = "<img src='" + product.url_image + "' style='width: 100px' >";


            var row = "<tr>";
            row+="<td>"+image+"</td>";
            row += "<td>" + name + "</td>";
            row += "<td>" + category + "</td>";
            row += "<td class='text-center'>" + "<a data-toggle=\"modal\" href=\"#Modal_add\">ویرایش</a>" + "  "+"<a href=\"#\">حذف</a>" + "</td>";
            row += "</tr>";
            $tbody.append(row);

        })


    })


})

