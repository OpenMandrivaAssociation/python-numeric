Summary:	Python numerical facilities 
Name:		python-numeric
Version:	24.2
Release:	9
License:	BSD-like
URL:		https://www.pfdubois.com/numpy/
Group:		Development/Python
Source0:	Numeric-%{version}.tar.bz2
Source1:	numpy.pdf.bz2
Patch0:		Numeric-24.2-linkage.patch
Requires:	python2
BuildRequires:	python2-devel

%description
A collection of extension modules to provide high-performance multidimensional
numeric arrays to the Python programming language.

%package	devel
Group:		Development/Python
Summary:	Python numerical facilities
Requires:	python-devel
Requires:	%{name} = %{version}-%{release}

%description	devel
A collection of extension modules to provide high-performance multidimensional
numeric arrays to the Python programming language.

Development files.

%prep
%setup -n Numeric-%{version} -q
%patch0 -p1
cp %{SOURCE1} .
bunzip2 numpy.pdf.bz2

%build
export CFLAGS="%{optflags}"
python setup.py build
for Package in FFT MA RNG; do
    (cd Packages/$Package; python setup.py build)
done

%install
python setup.py install --root=%{buildroot}
for Package in FFT MA RNG; do
    (cd Packages/$Package; python setup.py install --root=%{buildroot} --optimize=2)
done

%files
%doc MANIFEST README changes.txt
%{python_sitearch}/Numeric*
%ifarch x86_64
%{python_sitelib}/Numeric*
%endif

%files devel
%doc Demo Test numpy.pdf
%{_includedir}/python*/Numeric


%changelog
* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 24.2-7mdv2011.0
+ Revision: 590082
- rebuild for python 2.7

* Sun Aug 09 2009 Funda Wang <fwang@mandriva.org> 24.2-6mdv2010.0
+ Revision: 412894
- fix build

* Thu Dec 25 2008 Michael Scherer <misc@mandriva.org> 24.2-6mdv2009.1
+ Revision: 318467
- rebuild for new python

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 24.2-5mdv2009.0
+ Revision: 136454
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 24.2-5mdv2008.0
+ Revision: 82467
- rebuild with optflags
  use macros in file list


* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 24.2-4mdv2007.0
+ Revision: 87991
- rebuild

* Thu Oct 26 2006 Lev Givon <lev@mandriva.org> 24.2-3mdv2007.0
+ Revision: 72892
- Remove old python-numpy provides/obsoletes
  (which clash with newer python-numpy package)
- Import python-numeric

* Sat Aug 12 2006 Emmanuel Andry <eandry@mandriva.org> 24.2-2mdv2007.0
- fix 86_64 packaging

* Fri Mar 10 2006 Jerome Soyer <saispo@mandriva.org> 24.2-1mdk
- New release 24.2

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 24.0-2mdk
- Rebuild

* Fri Jul 15 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 24.0-1mdk
- 24.0
- fix requires
- %%mkrel

* Sat Dec 04 2004 Michael Scherer <misc@mandrake.org> 23.1-3mdk
- Rebuild for new python

* Tue Dec 16 2003 Lenny Cartier <lenny@mandrakesoft.com> 23.1-2mdk
- requires python-devel

* Fri Dec 12 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 23.1-1mdk
- 23.1

