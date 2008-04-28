
%define plugin	console
%define name	vdr-plugin-%plugin
%define version	0.6.0
%define rel	14

Summary:	VDR plugin: Expands VDR to a Console on TV
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://ricomp.de/vdr/
Source:		http://ricomp.de/vdr/vdr-%plugin-%version.tar.bz2
Patch1:		http://deela.cc.fh-lippe.de/files/vdr-console/console-0.6.0.patch
Patch2:		03_command_from_cli.dpatch
Patch3:		93_console-1.5.0.dpatch
Patch4:		console-0.6.0-i18n-1.6.patch
Patch5:		94_console-1.6.0.dpatch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Your  TV  screen  and a keyboard  that  are  connected to a VDR box  are
building a terminal. With this terminal you can manage several consoles.
In the OSD  of VDR you can  open as many  consoles as you want. In  each
console you can start a program that runs in the background. Your inputs
to the keyboard are  redirected to the current  selected console as well
as the output that these  programs generate are redirected into the OSD.

%prep
%setup -q -n %plugin-%version
%patch1 -p4 -b .1318
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# specify the program which is called when you start the plugin
var=COMMAND
param='-c COMMAND'
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY TODO


