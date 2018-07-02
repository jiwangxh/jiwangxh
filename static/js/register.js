$(function () {
    var error_name = false;
    var error_password = false;
    var error_check_password = false;

    $('#user_name').blur(function () {
        check_user_name();
    });

    $('#password').blur(function () {
        check_password();
    });

    $('#cpassword').blur(function () {
        check_cpassword();
    });

    function check_user_name() {
        var len = $('#user_name').val().length;
        if (len<5||len>20){
            $('#user_name').next().html('输入5-20个字符的用户名')
            $('#user_name').next().show();
            error_name = true;
        }
        else {
            $.get('/register_exist/?uname='+$('#user_name').val(), function (data) {
                if(data.count==1){
                    $('#user_name').next().html('用户已存在了').show();
                    error_name = true;
                }else{
                    $('#user_name').next().hide();
                    error_name = false;
                }

            });
        }
    }

    function check_password() {
        var len = $('#password').val().length;
        if (len<8||len>20) {
            $('#password').next().html('密码最少8位，最长20位')
            $('#password').next().show();
            error_password = true;
        }
        else {
            $('#password').next().hide();
            error_password = false;
        }
    }


    function check_cpassword() {
        var pass = $('#password').val();
        var cpass = $('#cpassword').val();

        if (pass != cpass)
        {
            $('#cpassword').next().html('再次输入的密码不一致')
            $('#cpassword').next().show();
            error_check_password = true;
        }
        else {
            $('#cpassword').next().hide();
            error_check_password = false;
        }
    }

    $('.reg_form').submit(function () {
        check_user_name();
        check_password();
        check_cpassword();
        if (error_name == false && error_password == false && error_check_password == false) {
            return true;
        }
        else {
            return false;
        }

    });
})