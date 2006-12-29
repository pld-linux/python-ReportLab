%define		module	ReportLab
%define		_module reportlab
%define		fversion	%(echo %{version} |tr . _)
Summary:	Python library for generating PDFs and graphics
Summary(pl):	Modu³y Pythona do generowania PDF-ów oraz grafik
Name:		python-%{module}
Version:	1.21
Release:	1
License:	distributable
Group:		Libraries/Python
Source0:	http://www.reportlab.com/ftp/ReportLab_%{fversion}.tgz
# Source0-md5:	5bc101ff85e56096ea9584c0117a27a8
URL:		http://www.reportlab.com/
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python
Requires:	python-PIL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	%{module}

%description
A library written in Python that lets you generate platform
independant PDFs and graphics.
- PDF generation: uses Python, a clean OO language, layered
  architecture
- Graphics: provides primitive shapes, reusable widgets, sample
  collections including business chart and diagrams
- PythonPoint: a utility for generating PDF slides from a simple XML
  format

%description -l pl
Biblioteka napisana w Pythonie pozwalaj±ca na generowanie niezale¿nych
od platformy PDF-ów oraz grafik.
- Generowanie PDF: u¿ywa Pythona, przejrzystego jêzyka obiektowego o
  warstwowej architekturze
- Grafika: podstawowe figury geometryczne, kontrolki, a tak¿e
  przyk³ady, w³±czaj±c w to wykresy i diagramy
- PythonPoing: narzêdzie do generowania slajdów w formacie PDF z
  prostego formatu XML

%package examples
Summary:	Examples of ReportLab
Summary(pl):	Przyk³ady do ReportLab
Group:		Libraries/Python
%pyrequires_eq  python
Requires:       %{name} = %{version}-%{release}

%description examples
Examples of ReportLab

%description examples -l pl
Przyk³ady do biblioteki ReportLab

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

install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}}
install tools/py2pdf/py2pdf.py $RPM_BUILD_ROOT%{_bindir}
install tools/pythonpoint/pythonpoint.py $RPM_BUILD_ROOT%{_bindir}

mv demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}
mv graphics/samples $RPM_BUILD_ROOT%{_examplesdir}/%{name}/graphics-samples
mv tools/pythonpoint/demos $RPM_BUILD_ROOT%{_examplesdir}/%{name}/pythonpoint-demos

%py_postclean $RPM_BUILD_ROOT%{py_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc reportlab/README reportlab/docs/*.pdf reportlab/license*
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/%{_module}
%{py_sitescriptdir}/%{_module}/*.py[co]
%dir %{py_sitescriptdir}/%{_module}/extensions
%{py_sitescriptdir}/%{_module}/extensions/*.py[co]
%dir %{py_sitescriptdir}/%{_module}/fonts
%{py_sitescriptdir}/%{_module}/fonts/*.AFM
%{py_sitescriptdir}/%{_module}/fonts/*.PFB
%{py_sitescriptdir}/%{_module}/fonts/*.ttf
%{py_sitescriptdir}/%{_module}/fonts/*.txt
%dir %{py_sitescriptdir}/%{_module}/graphics
%{py_sitescriptdir}/%{_module}/graphics/*.py[co]
%dir %{py_sitescriptdir}/%{_module}/graphics/charts
%{py_sitescriptdir}/%{_module}/graphics/charts/*.py[co]
%dir %{py_sitescriptdir}/%{_module}/graphics/widgets
%{py_sitescriptdir}/%{_module}/graphics/widgets/*.py[co]
%dir %{py_sitescriptdir}/%{_module}/lib
%{py_sitescriptdir}/%{_module}/lib/*.py[co]
%dir %{py_sitescriptdir}/%{_module}/pdfbase
%{py_sitescriptdir}/%{_module}/pdfbase/*.py[co]
%dir %{py_sitescriptdir}/%{_module}/pdfgen
%{py_sitescriptdir}/%{_module}/pdfgen/*.py[co]
%dir %{py_sitescriptdir}/%{_module}/platypus
%{py_sitescriptdir}/%{_module}/platypus/*.py[co]
%dir %{py_sitescriptdir}/%{_module}/tools
%{py_sitescriptdir}/%{_module}/tools/*.py[co]
%{py_sitescriptdir}/%{_module}/tools/README
%dir %{py_sitescriptdir}/%{_module}/tools/docco
%{py_sitescriptdir}/%{_module}/tools/docco/*.py[co]
%{py_sitescriptdir}/%{_module}/tools/docco/README
%dir %{py_sitescriptdir}/%{_module}/tools/py2pdf
%{py_sitescriptdir}/%{_module}/tools/py2pdf/*.py[co]
%{py_sitescriptdir}/%{_module}/tools/py2pdf/*.jpg
%{py_sitescriptdir}/%{_module}/tools/py2pdf/*.txt
%{py_sitescriptdir}/%{_module}/tools/py2pdf/README
%dir %{py_sitescriptdir}/%{_module}/tools/pythonpoint
%{py_sitescriptdir}/%{_module}/tools/pythonpoint/*.py[co]
%{py_sitescriptdir}/%{_module}/tools/pythonpoint/README
%{py_sitescriptdir}/%{_module}/tools/pythonpoint/*.dtd
%dir %{py_sitescriptdir}/%{_module}/tools/pythonpoint/styles
%{py_sitescriptdir}/%{_module}/tools/pythonpoint/styles/*.py[co]

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}/demos
%dir %{_examplesdir}/%{name}/graphics-samples
%dir %{_examplesdir}/%{name}/pythonpoint-demos
%{_examplesdir}/%{name}/graphics-samples/*.py
%{_examplesdir}/%{name}/demos
%{_examplesdir}/%{name}/pythonpoint-demos
