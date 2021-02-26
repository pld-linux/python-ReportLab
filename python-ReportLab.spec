#
# Conditional build:
%bcond_without	doc	# PDF documentation
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

# TODO:
# - use system fonts (see files lists) or share fonts for both python versions
# - tools/docco and tools/pythonpoint as subpackages?

%define		module	ReportLab
Summary:	Python 2 library for generating PDFs and graphics
Summary(pl.UTF-8):	Moduły Pythona 2 do generowania PDF-ów oraz grafik
Name:		python-%{module}
Version:	3.5.34
Release:	2
License:	BSD-like
Group:		Libraries/Python
#Source0Download: https://bitbucket.org/rptlab/reportlab/downloads/?tab=tags
Source0:	https://files.pythonhosted.org/packages/source/r/reportlab/reportlab-%{version}.tar.gz
# Source0-md5:	77d37a7f9f785b3666206de0fbc44aab
Patch0:		%{name}-setup.patch
URL:		https://www.reportlab.com/dev/opensource/
BuildRequires:	freetype-devel >= 2
BuildRequires:	libart_lgpl-devel >= 2
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%endif
%{?with_doc:BuildRequires:	python-pillow >= 4.0.0}
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python-modules >= 1:2.7
Obsoletes:	ReportLab
Obsoletes:	python-ReportLab-barcode
Obsoletes:	python-ReportLab-renderPM
Obsoletes:	python-ReportLab-rl_accel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library written in Python that lets you generate platform
independant PDFs and graphics.
- PDF generation: uses Python, a clean OO language, layered
  architecture
- Graphics: provides primitive shapes, reusable widgets, sample
  collections including business chart and diagrams

%description -l pl.UTF-8
Biblioteka napisana w Pythonie pozwalająca na generowanie niezależnych
od platformy PDF-ów oraz grafik.
- Generowanie PDF: używa Pythona, przejrzystego języka obiektowego o
  warstwowej architekturze
- Grafika: podstawowe figury geometryczne, kontrolki, a także
  przykłady, w tym wykresy i diagramy

%package -n python3-%{module}
Summary:	Python 3 library for generating PDFs and graphics
Summary(pl.UTF-8):	Moduły Pythona 3 do generowania PDF-ów oraz grafik
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
A library written in Python that lets you generate platform
independant PDFs and graphics.
- PDF generation: uses Python, a clean OO language, layered
  architecture
- Graphics: provides primitive shapes, reusable widgets, sample
  collections including business chart and diagrams

%description -n python3-%{module} -l pl.UTF-8
Biblioteka napisana w Pythonie pozwalająca na generowanie niezależnych
od platformy PDF-ów oraz grafik.
- Generowanie PDF: używa Pythona, przejrzystego języka obiektowego o
  warstwowej architekturze
- Grafika: podstawowe figury geometryczne, kontrolki, a także
  przykłady, w tym wykresy i diagramy

%package apidocs
Summary:	API documentation for ReportLab module
Summary(pl.UTF_8):	Dokumentacja API modułu ReportLab
Group:		Documentation
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description apidocs
API documentation for ReportLab module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu ReportLab.

%package examples
Summary:	Examples for ReportLab
Summary(pl.UTF-8):	Przykłady do biblioteki ReportLab
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description examples
Examples for ReportLab.

%description examples -l pl.UTF-8
Przykłady do biblioteki ReportLab.

%prep
%setup -q -n reportlab-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%if %{with doc}
cd docs
PYTHONPATH=$(pwd)/../src %{__python} genAll.py
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/reportlab

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/reportlab/graphics/samples
%endif

%if %{with python3}
%py3_install

install -d $RPM_BUILD_ROOT%{py3_sitescriptdir}/reportlab

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/reportlab/graphics/samples
%endif

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# TODO: (whole) pythonpoint as subpackage?
#install -p tools/pythonpoint/pythonpoint.py $RPM_BUILD_ROOT%{_bindir}
#cp -a tools/pythonpoint/demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/pythonpoint-demos

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.txt README.txt
%dir %{py_sitescriptdir}/reportlab
%dir %{py_sitedir}/reportlab
%{py_sitedir}/reportlab-%{version}-py*.egg-info
%{py_sitedir}/reportlab/*.py[co]
%dir %{py_sitedir}/reportlab/fonts
%{py_sitedir}/reportlab/fonts/00readme.txt
# Dark Garden font (GPL v2+)
%{py_sitedir}/reportlab/fonts/DarkGardenMK.afm
%{py_sitedir}/reportlab/fonts/DarkGardenMK.pfb
%{py_sitedir}/reportlab/fonts/DarkGarden.sfd
%{py_sitedir}/reportlab/fonts/DarkGarden-*.txt
# Bitstream Vera font
%{py_sitedir}/reportlab/fonts/Vera*.ttf
%{py_sitedir}/reportlab/fonts/bitstream-vera-license.txt
# ?
%{py_sitedir}/reportlab/fonts/callig15.afm
%{py_sitedir}/reportlab/fonts/callig15.pfb
# Adobe fonts
%{py_sitedir}/reportlab/fonts/_a*____.pfb
%{py_sitedir}/reportlab/fonts/_e*____.pfb
%{py_sitedir}/reportlab/fonts/co*____.pfb
%{py_sitedir}/reportlab/fonts/sy______.pfb
%{py_sitedir}/reportlab/fonts/z?______.pfb
%dir %{py_sitedir}/reportlab/graphics
%attr(755,root,root) %{py_sitedir}/reportlab/graphics/_renderPM.so
%{py_sitedir}/reportlab/graphics/*.py[co]
%dir %{py_sitedir}/reportlab/graphics/barcode
%{py_sitedir}/reportlab/graphics/barcode/*.py[co]
%dir %{py_sitedir}/reportlab/graphics/charts
%{py_sitedir}/reportlab/graphics/charts/*.py[co]
%dir %{py_sitedir}/reportlab/graphics/widgets
%{py_sitedir}/reportlab/graphics/widgets/*.py[co]
%dir %{py_sitedir}/reportlab/lib
%attr(755,root,root) %{py_sitedir}/reportlab/lib/_rl_accel.so
%attr(755,root,root) %{py_sitedir}/reportlab/lib/pyHnj.so
%{py_sitedir}/reportlab/lib/*.py[co]
%{py_sitedir}/reportlab/lib/hyphen.mashed
%dir %{py_sitedir}/reportlab/pdfbase
%{py_sitedir}/reportlab/pdfbase/*.py[co]
%dir %{py_sitedir}/reportlab/pdfgen
%{py_sitedir}/reportlab/pdfgen/*.py[co]
%dir %{py_sitedir}/reportlab/platypus
%{py_sitedir}/reportlab/platypus/*.py[co]
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.txt README.txt
%dir %{py3_sitescriptdir}/reportlab
%dir %{py3_sitedir}/reportlab
%{py3_sitedir}/reportlab-%{version}-py*.egg-info
%{py3_sitedir}/reportlab/*.py
%{py3_sitedir}/reportlab/__pycache__
%dir %{py3_sitedir}/reportlab/fonts
%{py3_sitedir}/reportlab/fonts/00readme.txt
# Dark Garden font (GPL v2+)
%{py3_sitedir}/reportlab/fonts/DarkGardenMK.afm
%{py3_sitedir}/reportlab/fonts/DarkGardenMK.pfb
%{py3_sitedir}/reportlab/fonts/DarkGarden.sfd
%{py3_sitedir}/reportlab/fonts/DarkGarden-*.txt
# Bitstream Vera font
%{py3_sitedir}/reportlab/fonts/Vera*.ttf
%{py3_sitedir}/reportlab/fonts/bitstream-vera-license.txt
# ?
%{py3_sitedir}/reportlab/fonts/callig15.afm
%{py3_sitedir}/reportlab/fonts/callig15.pfb
# Adobe fonts
%{py3_sitedir}/reportlab/fonts/_a*____.pfb
%{py3_sitedir}/reportlab/fonts/_e*____.pfb
%{py3_sitedir}/reportlab/fonts/co*____.pfb
%{py3_sitedir}/reportlab/fonts/sy______.pfb
%{py3_sitedir}/reportlab/fonts/z?______.pfb
%dir %{py3_sitedir}/reportlab/graphics
%attr(755,root,root) %{py3_sitedir}/reportlab/graphics/_renderPM.cpython-*.so
%{py3_sitedir}/reportlab/graphics/*.py
%{py3_sitedir}/reportlab/graphics/__pycache__
%dir %{py3_sitedir}/reportlab/graphics/barcode
%{py3_sitedir}/reportlab/graphics/barcode/*.py
%{py3_sitedir}/reportlab/graphics/barcode/__pycache__
%dir %{py3_sitedir}/reportlab/graphics/charts
%{py3_sitedir}/reportlab/graphics/charts/*.py
%{py3_sitedir}/reportlab/graphics/charts/__pycache__
%dir %{py3_sitedir}/reportlab/graphics/widgets
%{py3_sitedir}/reportlab/graphics/widgets/*.py
%{py3_sitedir}/reportlab/graphics/widgets/__pycache__
%dir %{py3_sitedir}/reportlab/lib
%attr(755,root,root) %{py3_sitedir}/reportlab/lib/_rl_accel.cpython-*.so
%{py3_sitedir}/reportlab/lib/*.py
%{py3_sitedir}/reportlab/lib/__pycache__
%{py3_sitedir}/reportlab/lib/hyphen.mashed
%dir %{py3_sitedir}/reportlab/pdfbase
%{py3_sitedir}/reportlab/pdfbase/*.py
%{py3_sitedir}/reportlab/pdfbase/__pycache__
%dir %{py3_sitedir}/reportlab/pdfgen
%{py3_sitedir}/reportlab/pdfgen/*.py
%{py3_sitedir}/reportlab/pdfgen/__pycache__
%dir %{py3_sitedir}/reportlab/platypus
%{py3_sitedir}/reportlab/platypus/*.py
%{py3_sitedir}/reportlab/platypus/__pycache__
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/reportlab-userguide.pdf
%endif

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/demos
