
dcl_settings : default_dcl_settings { audit_level = 3; }

BatchPlotMain : dialog {
    label = "������ӡ";
    : row {
        : column {
            : boxed_radio_column {
                label = "ͼ����ʽ";
                : radio_button {
                    label = "����ͼ��(L): *_TITLE��";
                    key = "LzFrameRadio";
                    mnemonic = "L";
                }
                : radio_button {
                    label = "ͼ��(B): ͼ��Ϊ�ض�ͼ��";
                    key = "BlockRadio";
                    mnemonic = "B";
                }
                : radio_button {
                    label = "ͼ��(N): ָ��ͼ���վ���";
                    key = "LayerRadio";
                    mnemonic = "N";
                }
            }
            : boxed_column {
                label = "ͼ����ͼ��";
                key = "BlockAndLayerSettings";
                : button {
                    label = "��ͼ��ָ��ͼ���ͼ��(P)<";
                    key = "PickBtn";
                    mnemonic = "P";
                }
                :row {
	                : text {
	                    label = "ͼ����";
	                    value = "ͼ����";
	                }
	                : popup_list {
	                    key = "BlockNameEdit";
	                    fixed_height = false;
	                    fixed_width = true;
	                    width = 20;
	                }
	        }
                :row {
	                : text {
	                    label = "ͼ����";
	                    value = "ͼ����";
	                }
	               : popup_list {
	                    key = "LayerNameEdit";
	                    fixed_height = false;
	                    fixed_width = true;
	                    width = 20;
	                }
                }

            }
            : boxed_radio_column {
                label = "���ѡ��";
                : radio_button {
                    label = "ֱ��������ӡ(1)";
                    key = "PlotRadio";
                    mnemonic = "1";
                }
                : radio_button {
                    label = "�������ɲ���(2)";
                    key = "LayoutRadio";
                    mnemonic = "2";
                }
                : radio_button {
                    label = "����PLT�ļ�(3)";
                    key = "PlotFileRadio";
                    mnemonic = "3";
                }
                : radio_button {
                    label = "��ӡ���в���(4)";
                    key = "PlotLayoutRadio";
                    mnemonic = "4";
                }
            }
            : button {
                label = "ѡ��������ӡͼֽ(S) <";
                key = "SelectFramesBtn";
                mnemonic = "S";
            }
            : boxed_row {
                : text {
                    label = "ѡ��ͼֽ��0";
                    key = "StatusLabel";
                }
                : button {
                    label = "����(L)..";
                    key = "ShowFramesBtn";
                    mnemonic = "L";
                    is_enabled = false;
                }
            }
        }
        : column {
            children_alignment = right;
            : boxed_column {
                label = "��ӡ����";
                key = "PageSetupSettings";
                : row {
                    : popup_list {
                        label = "Ԥ������:";
                        key = "PageSetupPopup";
                    }
                    : button {
                        label = "��ӡ����(A)..";
                        key = "PageSetupBtn";
                        mnemonic = "A";
                        width = 20;
                        fixed_width = true;

                    }
                }
                : text {
                    label = "��ӡ�豸����";
                    value = "��ӡ�豸����";
                    key = "PlotterLabel";
                }
                : text {
                    label = "ֽ�Ŵ�С��";
                    value = "ֽ�Ŵ�С��";
                    key = "PaperLabel";
                }
                : row {
                    : text {
                        label = "��ӡ��ʽ��";
                        value = "��ӡ��ʽ��";
                        key = "PlotStyleLabel";
                    }
                    : edit_box {
                        label = "��ӡ����:";
                        value = "1";
                        key = "CopiesEdit";
                        width = 8;
                        fixed_width = true;
                    }
                }
            }
            : boxed_row {
                label = "��ӡ����";
                key = "ScaleSettings";
                : radio_row {
                    width = 40;
                    fixed_width = true;
                    : radio_button {
                        label = "�Զ�����";
                        key = "AutoScaleRadio";
                    }
                    : radio_button {
                        label = "�ʺ�ͼֽ";
                        key = "ScaleToFitRadio";
                    }
                    : radio_button {
                        label = "�̶�����:";
                        key = "FixScaleRadio";
                    }
                }
                : edit_box {
                    label = "1:";
                    value = "100";
                    key = "FixScaleEdit";
                }
            }
            : boxed_row {
                label = "ͼֽ��λ";
                key = "LocationSettings";
                  : toggle {
                       label = "�Զ���ת";
                       key = "AutoRotateCheck";
                  }
                  : toggle {
                       label = "����";
                       key = "UpsideDownCheck";
                  }
                  : radio_row {
                      : radio_button {
                          label = "�Զ�����";
                          key = "AutoCenterRadio";
                      }
                      : radio_button {
                          label = "ƫ��";
                          key = "OffsetRadio";
                      }
                  }
                 : edit_box {
                      label = "X=";
                      value = "0";
                      edit_width = 4;
                      key = "XOffsetEdit";
                  }
                  : edit_box {  
                      label = "Y=";  
                      value = "0";
                      edit_width = 4;
                      key = "YOffsetEdit";  
                  }  
            }
            : boxed_row {
                label = "��ӡ˳��";
                key = "PlotOrderSettings";
              : radio_row {
                      : radio_button {
                          label = "ѡ��˳��";
                          key = "SelectOrderRadio";
                      }
                      : radio_button {
                          label = "���ң�����";
                          key = "LeftToRightRadio";
                      }
                      : radio_button {
                          label = "���£�����";
                          key = "TopToBottomRadio";
                      }
              }
              : toggle {
                label = "����";
                key = "ReverseOrderCheck";
              }
            }
            : boxed_column {
                label = "��ӡ�ļ�";
                key = "PlotFileSettings";
                : row {
                    : edit_box {
                        label = "�ļ���ǰ׺:";
                        key = "PlotFilePrefixEdit";
                    }
                    : toggle {
                        label = "ɾ������ͬǰ׺����PLT�ļ�";
                        key = "DeletePlotFileCheck";
                    }
                }
                : row {
                    : edit_box {
                        label = "����λ��:";
                        key = "PlotFileFolderEdit";
                    }
                    : button {
                        label = "���..";
                        key = "BrowsePLTFolderBtn";
                        width = 15;
                        fixed_width = true;
                    }
                }
            }
            : boxed_column {
                label = "��������";
                key = "LayoutSettings";
                : row {
                    : edit_box {
                        label = "������ǰ׺:";
                        key = "LayoutPrefixEdit";
                    }
                    : toggle {
                        label = "ɾ��ͼ������ͬǰ׺���Ĳ���";
                        key = "DeleteLayoutCheck";
                    }
                }
                : toggle {
                    label = "�ڲ�����ǿ��ʹ��ģ�Ϳռ�����ͱ���";
                    key = "LtScaleCheck";
                }
            }
        }
    }
    : row {
        : button {
            label = "Ԥ��(R)";
            key = "PreviewBtn";
            mnemonic = "R";
            is_enabled = false;
        }
        spacer_1;
        spacer_1;
        spacer_1;
        spacer_1;
        spacer_1;
        spacer_1;
        : button {
            label = "ȷ��(O)";
            key = "OKBtn";
            mnemonic = "O";
            is_default = true;
            is_enabled = false;
        }
        : button {
            label = "ȡ��(C)";
            key = "CancelBtn";
            mnemonic = "C";
            is_cancel = true;
        }
        : button {
            label = "����(H)";
            key = "HelpBtn";
            mnemonic = "H";
        }
    }
}
