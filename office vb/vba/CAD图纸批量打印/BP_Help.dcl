
dcl_settings : default_dcl_settings { audit_level = 3; }

BP_Help : dialog {
    label = "批量打印-帮助";
    : boxed_column {
        : text {
            label = "模型空间批量打印程序 V2.0 ---- 秋枫，2003.11";
            alignment = centered;
        }
    }
    : list_box {
        key = "HelpList";
        width = 72;
        height = 24;
    }
    : row {
        spacer_1;
        : button {
            label = "确定(O)";
            key = "HelpOKBtn";
            is_default = true;
            width = 15;
            fixed_width = true;
        }
        spacer_1;
    }
}
