# TODO:
#  Check if docs/*.pdf is generated using _installed_ ReportLab
#  so build may fail if ReportLab is not installed on builder
%define		module	ReportLab
%define		fversion	%(echo %{version} |tr . _)
Summary:	Python library for generating PDFs and graphics
Summary(pl.UTF-8):	Moduły Pythona do generowania PDF-ów oraz grafik
Name:		python-%{module}
Version:	2.3
Release:	2
License:	distributable
Group:		Libraries/Python
Source0:	http://www.reportlab.org/ftp/ReportLab_%{fversion}.tar.gz
# Source0-md5:	057b846bd3b7b2c3498bf14f6a523632
Patch0:		%{name}-setup.patch
URL:		http://www.reportlab.org/
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python
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
  przykłady, włączając w to wykresy i diagramy
- PythonPoing: narzędzie do generowania slajdów w formacie PDF z
  prostego formatu XML

%package examples
Summary:	Examples for ReportLab
Summary(pl.UTF-8):	Przykłady do biblioteki ReportLab
Group:		Libraries/Python
%pyrequires_eq	python
Requires:	%{name} = %{version}-%{release}

%description examples
Examples for ReportLab.

%description examples -l pl.UTF-8
Przykłady do biblioteki ReportLab.

%prep
%setup -q -n ReportLab_%{fversion}

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
python setup.py build
cd docs
PYTHONPATH=../src python genAll.py
cd ..

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}
install tools/pythonpoint/pythonpoint.py $RPM_BUILD_ROOT%{_bindir}

cp -a demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a tools/pythonpoint/demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/pythonpoint-demos

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/reportlab/demos
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/reportlab/docs
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/reportlab/graphics/samples
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/reportlab/test

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt LICENSE.txt docs/*.pdf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{py_sitedir}/_renderPM.so
%attr(755,root,root) %{py_sitedir}/_rl_accel.so
%attr(755,root,root) %{py_sitedir}/pyHnj.so
%attr(755,root,root) %{py_sitedir}/sgmlop.so
%dir %{py_sitedir}/reportlab
%if "%{py_ver}" > "2.4"
%{py_sitedir}/reportlab-%{version}-py*.egg-info
%endif
%{py_sitedir}/reportlab/*.py[co]
%dir %{py_sitedir}/reportlab/fonts
%{py_sitedir}/reportlab/fonts/*.afm
%{py_sitedir}/reportlab/fonts/*.pfb
%{py_sitedir}/reportlab/fonts/*.sfd
%{py_sitedir}/reportlab/fonts/*.ttf
%{py_sitedir}/reportlab/fonts/*.txt
%dir %{py_sitedir}/reportlab/graphics
%{py_sitedir}/reportlab/graphics/*.py[co]
%dir %{py_sitedir}/reportlab/graphics/charts
%{py_sitedir}/reportlab/graphics/charts/*.py[co]
%dir %{py_sitedir}/reportlab/graphics/barcode
%{py_sitedir}/reportlab/graphics/barcode/*.py[co]
%dir %{py_sitedir}/reportlab/graphics/widgets
%{py_sitedir}/reportlab/graphics/widgets/*.py[co]
%dir %{py_sitedir}/reportlab/lib
%{py_sitedir}/reportlab/lib/*.py[co]
%{py_sitedir}/reportlab/lib/*.mashed
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
