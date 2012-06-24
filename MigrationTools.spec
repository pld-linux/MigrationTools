# $Revision: 1.12 $Date: 2003-10-09 12:21:37 $
%include        /usr/lib/rpm/macros.perl
Summary:	LDAP Migration Tools
Summary(pl):	Narz�dzia do migraacji do LDAP
Name:		ldap-MigrationTools
Version:	45
Release:	2
License:	custom
Group:		Base
Source0:	http://www.padl.com/download/MigrationTools.tgz
# Source0-md5:	2355e54f17a1fdc87b0d56ed9ea3e115
Source1:	http://www.padl.com/download/MigrationTools.txt
URL:		http://www.padl.com/tools.html
Patch0:		MigrationTools-38-instdir.patch
Patch1:		MigrationTools-36-mktemp.patch
Patch2:		MigrationTools-27-simple.patch
Patch3:		MigrationTools-26-suffix.patch
Patch4:		MigrationTools-44-schema.patch
Patch5:		MigrationTools-services.patch
BuildRequires:	rpm-perlprov
Requires:	openldap
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MigrationTools are a set of Perl scripts for migrating users,
groups, aliases, hosts, netgroups, networks, protocols, RPCs, and
services from existing nameservices (flat files, NIS, and NetInfo) to
LDAP.

%description -l pl
MigrationTools to zestaw skrypt�w perlowych do migracji u�ytkownik�w,
grup, host�w, grup sieciowych, sieci, protoko��w, RPC i serwis�w z
istniej�cych serwis�w nazw (zwyk�ych plik�w, NIS, NetInfo) do LDAP.

%prep
%setup -qn MigrationTools-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
install %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/MigrationTools
install *.sh *.pl *.ph $RPM_BUILD_ROOT%{_datadir}/MigrationTools

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc MigrationTools.txt README
%dir %{_datadir}/MigrationTools
%attr(755,root,root) %{_datadir}/MigrationTools/*.sh
%attr(755,root,root) %{_datadir}/MigrationTools/*.pl
%config(noreplace) %verify(not md5 size mtime) %{_datadir}/MigrationTools/*.ph
