$(document).ready(function () {
    var $tbody = $("#order_list");
    var $tbody_2 = $("#order_details");
    var Arry = [
        $('[name="customer_name"]'),
        $('[name="address"]'),
        $('[name="phone"]'),
        $('[name="time_give"]'),
        $('[name="time_record"]')
    ];

    function createRow(order) {
        var id = order._id;
        var fullName = order.customer_first_name + " " + order.customer_last_name;
        totalCost = order.total_costs;
        timeRecord = order.time_record;

        var row = "<tr id='" + id + "'>";
        row += "<td>" + fullName + "</td>";
        row += "<td>" + totalCost + "</td>";
        row += "<td>" + timeRecord + "</td>";
        row +=
            "<td class='text-center'>" +
            '<a data-toggle="modal" href="#Modal_order"> بررسی سفارش </a>' +
            "</td>";
        row += "</tr>";
        $tbody.append(row);

        handleEditLink(order);
    }

    function createRow_2(order) {


        for (let i = 0; i < order.items.length; ++i) {
            $.ajax({
            url:'/api/product/return_product_id',
            type:"POST",
            data:{name_product:order.items[i].name_product},
            success:function (resp) {
                if (resp[0]["_id"]=="#"){
                    product_id="#"
                }
                else{
                    product_id="/product/"+resp[0]["_id"]
                }
                var name_product = order.items[i].name_product;
                var quantity = order.items[i].quantity;
                var price = order.items[i].price;
                var name_inventory = order.items[i].name_inventory;
                var row = "<tr id='" + order._id + "'>";
                row += "<td>" + "<a href='"+product_id+"'>"+name_product +"</a>"+ "</td>";
                row += "<td>" + new Intl.NumberFormat().format(price) + "</td>";
                row += "<td>" + quantity + "</td>";
                row += "<td>" + name_inventory + "</td>";
                row += "</tr>";
                $tbody_2.append(row);
            }

            })


        }
    }

    function handleEditLink(order) {
        $(document.getElementById(order._id))
            .find('a[href="#Modal_order"]')
            .click(function () {
                $.ajax({
                    url: "/api/order/list",
                    success: function (resp) {
                        var fullName =
                            order.customer_first_name + " " + order.customer_last_name;
                        var customer_name = "<div>" + fullName + "</div>";
                        var address = "<div>" + order.address + "</div>";
                        var phone = "<div>" + order.phone + "</div>";
                        var time_give = "<div>" + order.time_give + "</div>";
                        var time_record = "<div>" + order.time_record + "</div>";
                        Arry.forEach((div) => div.children().last().remove());
                        $('[name="customer_name"]').append(customer_name);
                        $('[name="address"]').append(address);
                        $('[name="phone"]').append(phone);
                        $('[name="time_give"]').append(time_give);
                        $('[name="time_record"]').append(time_record);
                        $tbody_2.empty();
//                        console.log(resp);
                        createRow_2(order)
                    }
                });
            });
    }

    $.get("/api/order/list", function (resp) {
        console.log(resp);
        resp.forEach((order) => createRow(order));
    });
});
