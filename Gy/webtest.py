from gooey import Gooey, GooeyParser


@Gooey(
    richtext_controls=True,                 # 打开终端对颜色支持
    program_name="环境切换",        # 程序名称
    encoding="utf-8",                       # 设置编码格式，打包的时候遇到问题
    progress_regex=r"^progress: (\d+)%$"    # 正则，用于模式化运行时进度信息
)
def main():
    settings_msg = '啥玩意'
    parser = GooeyParser(description=settings_msg)

    subs = parser.add_subparsers(help='commands', dest='command')

    my_parser = subs.add_parser('环境切换')
    my_parser.add_argument("connect", metavar='运行环境',help="请选择环境",choices=['测试环境','UAT环境'], default='测试环境')
    my_parser.add_argument("serialNumber", metavar='账号',help="请输入账号",default='')
    my_parser.add_argument("serialNumber", metavar='密码',help='请输入密码',default='')
    my_parser.add_argument("serialNumber", metavar='验证码', help='请输入验证码', default='')


     # siege_parser = subs.add_parser('进度条控制')
     # siege_parser.add_argument('num',help='请输入数字',default=1000)

    args = parser.parse_args()
    print(args, flush=True)    # flush=True在打包的时候会用到


if __name__ == '__main__':
    main()