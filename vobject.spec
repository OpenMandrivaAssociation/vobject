Summary:	Python module for parsing and generating vCard files
Name:		vobject
Version:	0.7.1
Release:	%mkrel 3
License:	ASL 1.1
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --compile --optimize=2

%post

%postun

%clean
rm -rf %{buildroot}

%files -n python-%{name}
%defattr(-,root,root)
%doc LICENSE.txt README.txt ACKNOWLEDGEMENTS.txt
%{py_puresitedir}/%{name}
%{_bindir}/ics_diff
%{_bindir}/change_tz
%{py_puresitedir}/%{name}-%{version}-py%{pyver}.egg-info

