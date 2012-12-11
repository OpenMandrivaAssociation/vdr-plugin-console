
%define plugin	console
%define name	vdr-plugin-%plugin
%define version	0.6.0
%define rel	16

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




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.6.0-16mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.6.0-15mdv2009.1
+ Revision: 359701
- rediff i18n patch
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.6.0-14mdv2009.0
+ Revision: 197914
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.6.0-13mdv2009.0
+ Revision: 197646
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- add a --command option (P2 from e-tobi)
- adapt for api changes of vdr 1.5.0 (P3 from e-tobi)
- adapt for api changes of vdr 1.6.0 (P5 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.6.0-12mdv2008.1
+ Revision: 145052
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.6.0-11mdv2008.1
+ Revision: 103078
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.6.0-10mdv2008.0
+ Revision: 49984
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.6.0-9mdv2008.0
+ Revision: 42071
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 8mdv2008.0-current
+ Revision: 22733
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.6.0-7mdv2007.0
+ Revision: 90906
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.6.0-6mdv2007.1
+ Revision: 73978
- rebuild for new vdr
- Import vdr-plugin-console

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.6.0-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.6.0-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.6.0-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.6.0-2mdv2007.0
- rebuild for new vdr

* Wed Jun 21 2006 Anssi Hannula <anssi@mandriva.org> 0.6.0-1mdv2007.0
- initial Mandriva release

