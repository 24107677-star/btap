from auth_ui import auth_window

def main():
    role = auth_window()   # nhận role trả về sau khi login
    
    if role == "admin":
        print(">>> Đăng nhập với quyền ADMIN")
        # TODO: mở giao diện admin
        # open_admin_ui()
        
    elif role == "customer":
        print(">>> Đăng nhập với quyền KHÁCH HÀNG")
        # TODO: mở giao diện khách
        # open_customer_ui()

    else:
        print("Không nhận được thông tin đăng nhập")


if __name__ == "__main__":
    main()

