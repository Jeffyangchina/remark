
dcl_settings : default_dcl_settings { audit_level = 3; }

BP_Help : dialog {
    label = "������ӡ-����";
    : boxed_column {
        : text {
            label = "ģ�Ϳռ�������ӡ���� V2.0 ---- ��㣬2003.11";
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
            label = "ȷ��(O)";
            key = "HelpOKBtn";
            is_default = true;
            width = 15;
            fixed_width = true;
        }
        spacer_1;
    }
}
