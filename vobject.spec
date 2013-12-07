Summary:	Python module for parsing and generating vCard files
Name:		vobject
Version:	0.7.1
%define subrel 1
Release:	9
License:	ASL 1.1
Group:		Development/Python
URL:		http://vobject.skyhouseconsulting.com
Source0:	http://vobject.skyhouseconsulting.com/%{name}-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
vobject is intended to be a full featured Python package for parsing
and generating vCard and vCalendar files.

Currently, iCalendar files are supported and well tested. vCard 3.0
files are supported, and all data should be imported, but only a few
components are understood in a sophisticated way.

%package -n python-%{name}

Summary:	Python module for parsing and generating vCard files
Group:		Development/Python
Requires:	python-dateutil
BuildArch:	noarch

%description -n python-%{name}
vobject is intended to be a full featured Python package for parsing
and generating vCard and vCalendar files.

Currently, iCalendar files are supported and well tested. vCard 3.0
files are supported, and all data should be imported, but only a few
components are understood in a sophisticated way.

%prep
%setup -q

%build

%install
python setup.py install --root=%{buildroot} --compile --optimize=2

%files -n python-%{name}
%defattr(-,root,root)
%doc LICENSE.txt README.txt ACKNOWLEDGEMENTS.txt
%{py_puresitedir}/%{name}
%{_bindir}/ics_diff
%{_bindir}/change_tz
%{py_puresitedir}/%{name}-%{version}-py%{py_ver}.egg-info



%changelog
* Tue Sep 20 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.1-3.1
- built for updates

* Sat Nov 06 2010 Jani Välimaa <wally@mandriva.org> 0.7.1-3mdv2011.0
+ Revision: 594309
- rebuild for python 2.7

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.7.1-2mdv2010.0
+ Revision: 445699
- rebuild

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 0.7.1-1mdv2009.1
+ Revision: 319471
- rebuild with python 2.6
- add new file to file list
- new release 0.7.1

* Sat Aug 09 2008 Thierry Vignaud <tv@mandriva.org> 0.6.0-2mdv2009.0
+ Revision: 269667
- rebuild early 2009.0 package (before pixel changes)

* Thu May 01 2008 Adam Williamson <awilliamson@mandriva.org> 0.6.0-1mdv2009.0
+ Revision: 199866
- include .pyc and .pyo files
- clean spec
- new release 0.6.0

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Tue Aug 21 2007 Adam Williamson <awilliamson@mandriva.org> 0.4.8-1mdv2008.0
+ Revision: 68633
- buildrequires python-setuptools
- Import vobject

