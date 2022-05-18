# RELEASE NOTE

## release 日期：2022-05-17

v1.10.0 release

- **breaking change**: 直接使用 `**kwargs` 来构造参数，避免部分构造函数的参数数量超过 255 导致的 3.7- 及以下版本的 Python3 无法使用 sdk 的问题, 如果使用 `param = Param(args1,args2,args3)` 形式构建参数，需要替换为 `param = Param(args1=args1,args2=args2,args3=args3)` 或者 `param = Param(**{'args1':args1,'args2':args2,'args3':args3})`
- feature: UserApi: [createRootUser]: 创建初始 root 用户，创建用户需要传递 role id，而获取 role id 需要鉴权，提供一个接口在没有账号被建立的情况下创建一个默认的 root 用户，不需要鉴权;
- feature: VmApi: [expand_vm_disk]: 提供扩容指定虚拟盘的能力;
- feature: VmApi: [eject_iso_from_vm_cd_rom]: 将 iso 从 vm cdrom 中卸载;
- feature: VmApi: [toggle_vm_cd_rom_disable]: 禁用、启用 vm cdrom;
- feature: VmApi: [update_vm_nic_basic_info]: 更新一个虚拟机网卡的常用信息，包括 IP 地址，网关地址，子网掩码，需要虚拟机工具的支持;
- feature: VmApi: [update_vm_nic_advance_info]: 更新一个虚拟机网卡的非常用信息，包括接入的虚拟网络，sriov 网卡的直连网卡，mac 地址，是否启用，以及是否开启镜像模式;
- feature: VmApi: [update_vm_advanced_options]: 更新虚拟机的高级信息，包括 CPU 兼容性，虚拟机时钟(UTC、LocalTime)，是否开启为 windows 优化，以及虚拟机显卡型号;
- optimize: 提供了更加完整的错误返回信息，包含了错误发生的位置，graphql operationName，并透传 tower server 状态码。
- optimize: 缩短了部分变量类型名称。
- bugfix: VmApi: [create_vm_from_template], []: 修复了无法在使用模板创建虚拟机时挂载已存在的虚拟机和 cd-rom 的问题，修正 MountDiskParams 中的 index 为可选项。
- bugfix: 使用了更加准确的数字类型，将以 Byte，HZ 为单位的数字类型从 Double 转为了 Long;
- bugfix: 修复 `waitTask` 在 task 出错时会轮询直到超时;
- bugfix: 将分类错误的 endpoint 移至正确的 api 下:
  - [get_iscsi_connections]: IscsiApi -> IscsiConnectionApi
  - [create_nvmf_subsystem]: DefaultApi -> NvmfSubsystemApi
  - [delete_nvmf_subsystem]: DefaultApi -> NvmfSubsystemApi
  - [update_nvmf_subsystem]: DefaultApi -> NvmfSubsystemApi
