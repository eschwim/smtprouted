Summary:    SMTP routing/proxy daemon
Name:       smtprouted
Version:    0.1
Release:    1%{?dist}
URL:        https://github.com/eschwim/smtprouted/
License:    MIT
Group:      Development/Languages
Source0:    smtprouted
Source1:    smtprouted.conf
Source2:    smtprouted.init
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:   python 

%description
A very performant python script for selectively forwarding email to        
different endpoints based on regular expression matching.  Can also provide
message de-duplication (i.e. it will only forward a message to the first   
MAIL TO: recipient that it receives, regardless of how many addresses      
are on the recipient list).  This script is perhaps most useful when acting
as the frontend for a catchall/mailsink postfix server used for testing    
email sending routines.                                                    

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 0755 %{SOURCE0} %{buildroot}%{_sbindir}/smtprouted
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/smtprouted.conf
install -D -m 0755 %{SOURCE2} %{buildroot}%{_initddir}/smtprouted

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sbindir}/smtprouted
%{_sysconfdir}/smtprouted.conf
%{_initddir}/smtprouted


%changelog
* Mon Sep 04 2014 Eric Schwimmer <eric@nerdvana.org> - 0.1-1
- Initial build
