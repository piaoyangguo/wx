layui.use('laydate', function () {
    var laydate = layui.laydate;

    var start = {
        //min: laydate.now(),
        //max: '2099-06-16 23:59:59',
        istoday: false,
        format: 'YYYY-MM-DD hh:mm:ss', //日期格式
        istime: true, //是否开启时间选择

        isclear: false, //是否显示清空
        issure: true, //是否显示确认

        choose: function (datas) {
            //end.min = datas; //开始日选好后，重置结束日的最小日期
            //end.start = datas //将结束日的初始值设定为开始日
        }
    };
    //try {
    //    document.getElementById("FromDate").onclick = function () {
    //        start.elem = this;
    //        laydate(start);
    //    }
    //    document.getElementById("ToDate").onclick = function () {
    //        start.elem = this;
    //        laydate(start);
    //    }
    //} catch (e) {
    //
    //}
    $(".layui_datetime").click(function () {
        start.elem = this;
        laydate(start);
    })
});