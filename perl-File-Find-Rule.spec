Name: 		perl-File-Find-Rule
Version: 	0.30
Release: 	9%{?dist}
Summary: 	Perl module implementing an alternative interface to File::Find
License: 	GPL+ or Artistic
Group: 		Development/Libraries
URL: 		http://search.cpan.org/dist/File-Find-Rule/
Source0: 	http://www.cpan.org/modules/by-module/File/File-Find-Rule-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: 	noarch
BuildRequires:	perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires: 	perl(Number::Compare)
BuildRequires: 	perl(Text::Glob)
BuildRequires:  perl(Test::More)

Requires:  	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
File::Find::Rule is a friendlier interface to File::Find.  It allows
you to build rules which specify the desired files and directories.

%prep
%setup -q -n File-Find-Rule-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%clean
rm -rf $RPM_BUILD_ROOT

%check
make test

%files
%defattr(-,root,root,-)
%doc Changes README
%{_bindir}/findrule
%{_mandir}/man1/*
%{perl_vendorlib}/File
%{_mandir}/man3/*

%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.30-9
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.30-6
- Rebuild for perl 5.10 (again)

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.30-5
- rebuild for new perl

* Tue Dec 11 2007 Ralf Corsépius <rc040203@freenet.de> - 0.30-4
- Add BR: perl(Test::More) (BZ 419631).

* Mon Sep 03 2007 Ralf Corsépius <rc040203@freenet.de> - 0.30-3
- Update license tag.
- Add BR: perl(ExtUtils::MakeMaker).

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.30-2
- Mass rebuild.

* Mon Jun 05 2006 Ralf Corsépius <rc040203@freenet.de> - 0.30-1
- Upstream update.

* Sun May 21 2006 Ralf Corsépius <rc040203@freenet.de> - 0.29-1
- Upstream update.

* Tue Feb 28 2006 Ralf Corsépius <rc040203@freenet.de> - 0.28-4
- Rebuild for perl-5.8.8.

* Tue Aug 16 2005 Ralf Corsepius <ralf@links2linux.de> - 0.28-3
- Spec cleanup.

* Wed Aug 10 2005 Ralf Corsepius <ralf@links2linux.de> - 0.28-2
- FE re-submission.

* Mon Mar 21 2005 Ralf Corsepius <ralf@links2linux.de> - 0.28-1
- FE submission.
