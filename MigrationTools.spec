# $Revision: 1.1 $Date: 2000-09-12 13:54:52 $
%include        /usr/lib/rpm/macros.perl
Summary:	LDAP Migration Tools 
Name:		ldap-MigrationTools
Version:	24
Release:	1
License:	Custom
Group:		Base
Group(pl):	Podstawowe
Source0:	http://www.padl.com/download/MigrationTools.tgz
Source1:	http://www.padl.com/download/MigrationTools.txt
URL:		http://www.padl.com/tools.html
BuildRequires:	rpm-perlprov
Requires:	openldap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
The MigrationTools are a set of Perl scripts for migrating users, groups,
aliases, hosts, netgroups, networks, protocols, RPCs, and services from
existing nameservices (flat files, NIS, and NetInfo) to LDAP.

%prep
%setup -qn MigrationTools-%{version}
install %{SOURCE1} .

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_datadir}/MigrationTools
install *.sh *.pl *.ph $RPM_BUILD_ROOT/%{_datadir}/MigrationTools

gzip -9nf MigrationTools.txt README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_datadir}/MigrationTools
%attr(755,root,root) %{_datadir}/MigrationTools/*.sh
%attr(755,root,root) %{_datadir}/MigrationTools/*.pl
%{_datadir}/MigrationTools/*.ph
