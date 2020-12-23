$(document).ready(function () {
    $tbody = $("#product_table")


    $.get('/api/product/list', function (resp) {
        resp.forEach(function (product) {
            var name = product.name_product;
            var category = product.category;
            var image = "<img src='" + product.url_image + "' style='width: 100px' >";
            var row = "<tr id='" + product._id + "'>";
            row += "<td>" + image + "</td>";
            row += "<td>" + name + "</td>";
            row += "<td>" + category + "</td>";
            row += "<td class='text-center'>" + "<a data-toggle=\"modal\" href=\"#Modal_add\">ویرایش</a>" + "  " + "<a  class='delete' href=\"#\">حذف</a>" + "</td>";
            row += "</tr>";
            $tbody.append(row);





                })


            $.get('/api/product/json_category',function (resp) {
                for (let i=0;resp[0].length;++i){
                    console.log(i)
                    console.table(resp[0][i])

                }


            $(".delete").click(function () {
                var $tr = $(this).closest('tr');
                url = '/api/product/delete/' + parseInt($tr.attr('id'))
                $.get(url)
                $($tr).remove();


            })

        })


    })


})

