# $Revision: 1.16 $Date: 2005-09-02 19:06:43 $
%include        /usr/lib/rpm/macros.perl
Summary:	LDAP Migration Tools
Summary(pl):	Narzêdzia do migraacji do LDAP
Name:		ldap-MigrationTools
Version:	46
Release:	0.1
License:	custom
Group:		Base
Source0:	http://www.padl.com/download/MigrationTools-%{version}.tgz
# Source0-md5:	dc80548f76d6aeba2b51b15751e08b21
Source1:	http://www.padl.com/download/MigrationTools.txt
Patch0:		MigrationTools-38-instdir.patch
Patch1:		MigrationTools-36-mktemp.patch
Patch2:		MigrationTools-27-simple.patch
Patch3:		MigrationTools-26-suffix.patch
Patch4:		MigrationTools-44-schema.patch
URL:		http://www.padl.com/tools.html
BuildRequires:	rpm-perlprov
Requires:	openldap
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MigrationTools are a set of Perl scripts for migrating users,
groups, aliases, hosts, netgroups, networks, protocols, RPCs, and
services from existing nameservices (flat files, NIS, and NetInfo) to
LDAP.

%description -l pl
MigrationTools to zestaw skryptów perlowych do migracji u¿ytkowników,
grup, hostów, grup sieciowych, sieci, protoko³ów, RPC i serwisów z
istniej±cych serwisów nazw (zwyk³ych plików, NIS, NetInfo) do LDAP.

%prep
%setup -qn MigrationTools-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
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
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/MigrationTools/*.ph
