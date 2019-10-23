#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Common namespace files for jaraco.* modules
Summary(pl.UTF-8):	Wspólna przestrzeń nazw dla modułów jaraco.*
Name:		python-jaraco
Version:	0
Release:	2
License:	MIT
Group:		Libraries/Python
# taken from jaraco.packaging 6.2
Source0:	jaraco.__init__.py
URL:		https://github.com/jaraco/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-modules
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common namespace files for jaraco.* modules.

%description -l pl.UTF-8
Wspólna przestrzeń nazw dla modułów jaraco.*.

%package -n python3-jaraco
Summary:	Common namespace files for jaraco.* modules
Summary(pl.UTF-8):	Wspólna przestrzeń nazw dla modułów jaraco.*
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-jaraco
Common namespace files for jaraco.* modules.

%description -n python3-jaraco -l pl.UTF-8
Wspólna przestrzeń nazw dla modułów jaraco.*.

%prep

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/jaraco
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{py_sitescriptdir}/jaraco/__init__.py

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{py3_sitescriptdir}/jaraco
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{py3_sitescriptdir}/jaraco/__init__.py

%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/jaraco
%{py_sitescriptdir}/jaraco/__init__.py[co]
%endif

%if %{with python3}
%files -n python3-jaraco
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/jaraco
%{py3_sitescriptdir}/jaraco/__init__.py
%{py3_sitescriptdir}/jaraco/__pycache__
%endif
