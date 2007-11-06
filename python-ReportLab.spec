%define		module	ReportLab
%define		fversion	%(echo %{version} |tr . _)
Summary:	Python library for generating PDFs and graphics
Summary(pl.UTF-8):	Moduły Pythona do generowania PDF-ów oraz grafik
Name:		python-%{module}
Version:	2.1
Release:	1
License:	distributable
Group:		Libraries/Python
Source0:	http://www.reportlab.com/ftp/ReportLab_%{fversion}.tgz
# Source0-md5:	d6eefe9e6e06aaa1315462045c9726ba
URL:		http://www.reportlab.com/
BuildRequires:	python-devel >= 1:2.4
%pyrequires_eq	python
Requires:	python-PIL
Obsoletes:	ReportLab
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
%setup -q -n reportlab_%{fversion}

%build
cd reportlab
CFLAGS="%{rpmcflags}"; export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
cd reportlab
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}
install tools/py2pdf/py2pdf.py $RPM_BUILD_ROOT%{_bindir}
install tools/pythonpoint/pythonpoint.py $RPM_BUILD_ROOT%{_bindir}

cp -a demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a graphics/samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/graphics-samples
cp -a tools/pythonpoint/demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/pythonpoint-demos

rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/reportlab/demos
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/reportlab/docs
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/reportlab/graphics/samples
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/reportlab/test
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/reportlab/tools/pythonpoint/demos

%py_postclean $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc reportlab/README reportlab/docs/*.pdf reportlab/license*
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/Reportlab-%{version}-py*.egg-info
%{py_sitedir}/reportlab
# mess part 2: docs and static files
%dir %{py_sitescriptdir}/reportlab
%dir %{py_sitescriptdir}/reportlab/fonts
%{py_sitescriptdir}/reportlab/fonts/*.AFM
%{py_sitescriptdir}/reportlab/fonts/*.PFB
%{py_sitescriptdir}/reportlab/fonts/*.ttf
%{py_sitescriptdir}/reportlab/fonts/*.txt
%dir %{py_sitescriptdir}/reportlab/tools
%{py_sitescriptdir}/reportlab/tools/README
%dir %{py_sitescriptdir}/reportlab/tools/docco
%{py_sitescriptdir}/reportlab/tools/docco/README
%dir %{py_sitescriptdir}/reportlab/tools/py2pdf
%{py_sitescriptdir}/reportlab/tools/py2pdf/*.jpg
%{py_sitescriptdir}/reportlab/tools/py2pdf/*.txt
%{py_sitescriptdir}/reportlab/tools/py2pdf/README
%dir %{py_sitescriptdir}/reportlab/tools/pythonpoint
%{py_sitescriptdir}/reportlab/tools/pythonpoint/README
%{py_sitescriptdir}/reportlab/tools/pythonpoint/*.dtd

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}-%{version}
%dir %{_examplesdir}/%{name}-%{version}/graphics-samples
%{_examplesdir}/%{name}-%{version}/graphics-samples/*.py
%{_examplesdir}/%{name}-%{version}/demos
%{_examplesdir}/%{name}-%{version}/pythonpoint-demos