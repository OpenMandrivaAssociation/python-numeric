%define	name	python-numeric
%define	version	24.2
%define rel	4
%define	release %mkrel %{rel}

Summary:	Python numerical facilities 
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD-like
URL:		http://www.pfdubois.com/numpy/
Group:		Development/Python
Source0:	Numeric-%{version}.tar.bz2
Source1:	numpy.pdf.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}buildroot
Requires:	python >= 2.0
BuildRequires:	python-devel

%description
A collection of extension modules to provide high-performance multidimensional
numeric arrays to the Python programming language.

%package	devel
Group:		Development/Python
Summary:	Python numerical facilities
Requires:	python-devel %{name} = %{version}

%description	devel
A collection of extension modules to provide high-performance multidimensional
numeric arrays to the Python programming language.

Devel files

%prep
%setup -n Numeric-%{version} -q
cp %{SOURCE1} .
bunzip2 numpy.pdf.bz2


%build
python setup.py build
for Package in FFT LALITE MA RANLIB RNG; do
    (cd Packages/$Package; python setup.py build)
done


%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}
for Package in FFT LALITE MA RANLIB RNG; do
    (cd Packages/$Package; python setup.py install --root=%{buildroot})
done


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root)
%doc MANIFEST README changes.txt
%{_libdir}/python*/site-packages/Numeric/*
%{_libdir}/python*/site-packages/Numeric.pth

%ifarch x86_64
/usr/lib/python*/site-packages/Numeric/*
/usr/lib/python*/site-packages/Numeric.pth
%endif

%files devel
%defattr(-, root, root)
%doc Demo Test numpy.pdf
%{_includedir}/python*/Numeric


