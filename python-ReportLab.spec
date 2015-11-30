#
# Conditional build:
%bcond_without	doc	# PDF documentation

# TODO:
# - python3 (3.3+) package
# - use system fonts:
#   /usr/lib/python2.7/site-packages/reportlab/fonts/VeraBI.ttf
# - Check if docs/*.pdf is generated using _installed_ ReportLab
#   so build may fail if ReportLab is not installed on builder
# - Standard T1 font curves (source1) maybe should be packaged in other package?

%define		module	ReportLab
Summary:	Python library for generating PDFs and graphics
Summary(pl.UTF-8):	Moduły Pythona do generowania PDF-ów oraz grafik
Name:		python-%{module}
Version:	3.0
Release:	4
License:	BSD-like
Group:		Libraries/Python
#Source0Download: https://bitbucket.org/rptlab/reportlab/downloads
Source0:	https://bitbucket.org/rptlab/reportlab/get/ReportLab_3_0.tar.bz2
# Source0-md5:	2c902ed7f6bf029cd0946858f0b2c07e
Source1:	http://www.reportlab.com/ftp/fonts/pfbfer.zip
# Source1-md5:	35d20e26490cb2a8646fab6276ac6a4c
Patch0:		%{name}-setup.patch
URL:		http://www.reportlab.org/
BuildRequires:	freetype-devel >= 2
BuildRequires:	libart_lgpl-devel >= 2
%{?with_doc:BuildRequires:	python-PIL}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	unzip
Requires:	python >= 1:2.7
Requires:	python-PIL
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
- PythonPoint: a utility for generating PDF slides from a simple XML
  format

%description -l pl.UTF-8
Biblioteka napisana w Pythonie pozwalająca na generowanie niezależnych
od platformy PDF-ów oraz grafik.
- Generowanie PDF: używa Pythona, przejrzystego języka obiektowego o
  warstwowej architekturze
- Grafika: podstawowe figury geometryczne, kontrolki, a także
  przykłady, w tym wykresy i diagramy
- PythonPoint: narzędzie do generowania slajdów w formacie PDF z
  prostego formatu XML

%package examples
Summary:	Examples for ReportLab
Summary(pl.UTF-8):	Przykłady do biblioteki ReportLab
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Examples for ReportLab.

%description examples -l pl.UTF-8
Przykłady do biblioteki ReportLab.

%prep
%setup -q -n rptlab-reportlab-6382a792db9e

%{__unzip} -qq -d src/reportlab/fonts %{SOURCE1}

%build
%py_build
%if %{with doc}
cd docs
PYTHONPATH=$(pwd)/../src %{__python} genAll.py
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py_install

install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}
install -p tools/pythonpoint/pythonpoint.py $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/reportlab

cp -a demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a tools/pythonpoint/demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/pythonpoint-demos

%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/reportlab/graphics/samples

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.txt %{?with_doc:docs/reportlab-userguide.pdf}
%attr(755,root,root) %{_bindir}/pythonpoint.py
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

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/demos
%{_examplesdir}/%{name}-%{version}/pythonpoint-demos
