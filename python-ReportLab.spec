%define		module	ReportLab
%define		fversion	%(echo %{version} |tr . _)
Summary:	Python library for generating PDFs and graphics
Summary(pl):	Modu³y Pythona do generowania PDF-ów oraz grafik
Name:		python-%{module}
Version:	1.19
Release:	4
License:	distributable
Group:		Libraries/Python
Source0:	http://www.reportlab.com/ftp/ReportLab_%{fversion}.tgz
# Source0-md5:	02eeec6481f71918bf469a78edc4437c
URL:		http://www.reportlab.com/
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	rpm-pythonprov
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

%prep
%setup -q -n reportlab-%{fversion}

%build
cd reportlab
%{__make} -C lib -f Makefile.pre.in boot \
	LIBP="%{py_libdir}"
perl -pi -e "s|\@DEFS\@||" lib/Makefile
%{__make} -C lib \
	OPT="%{rpmcflags}" \
	CC="%{__cc}" \
	LIBP="%{py_libdir}"

%install
rm -rf $RPM_BUILD_ROOT
cd reportlab
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{py_sitedir}/%{module}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -rf test
cp -aR * $RPM_BUILD_ROOT%{py_sitedir}/%{module}
rm -rf $RPM_BUILD_ROOT%{py_sitedir}/%{module}/{demos,docs}
cp -a demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

echo "%{module}" > $RPM_BUILD_ROOT%{py_sitedir}/reportlab.pth
ln -s %{module} $RPM_BUILD_ROOT%{py_sitedir}/reportlab

install tools/py2pdf/py2pdf.py $RPM_BUILD_ROOT%{_bindir}
install tools/pythonpoint/pythonpoint.py $RPM_BUILD_ROOT%{_bindir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc reportlab/docs/* reportlab/license*
%{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/*
%{py_sitedir}/*.pth
%dir %{py_sitedir}/reportlab
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/extensions
%{py_sitedir}/%{module}/extensions/*.py[co]
%dir %{py_sitedir}/%{module}/fonts
%{py_sitedir}/%{module}/fonts/*.AFM
%{py_sitedir}/%{module}/fonts/*.PFB
%{py_sitedir}/%{module}/fonts/*.ttf
%{py_sitedir}/%{module}/fonts/*.txt
%dir %{py_sitedir}/%{module}/graphics
%{py_sitedir}/%{module}/graphics/*.py[co]
%dir %{py_sitedir}/%{module}/graphics/charts
%{py_sitedir}/%{module}/graphics/charts/*.py[co]
%dir %{py_sitedir}/%{module}/graphics/widgets
%{py_sitedir}/%{module}/graphics/widgets/*.py[co]
%dir %{py_sitedir}/%{module}/lib
%{py_sitedir}/%{module}/lib/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/lib/*.so
%dir %{py_sitedir}/%{module}/pdfbase
%{py_sitedir}/%{module}/pdfbase/*.py[co]
%dir %{py_sitedir}/%{module}/pdfgen
%{py_sitedir}/%{module}/pdfgen/*.py[co]
%dir %{py_sitedir}/%{module}/platypus
%{py_sitedir}/%{module}/platypus/*.py[co]
%dir %{py_sitedir}/%{module}/tools
%{py_sitedir}/%{module}/tools/*.py[co]
%dir %{py_sitedir}/%{module}/tools/docco
%{py_sitedir}/%{module}/tools/docco/*.py[co]
%dir %{py_sitedir}/%{module}/tools/py2pdf
%{py_sitedir}/%{module}/tools/py2pdf/*.py[co]
%{py_sitedir}/%{module}/tools/py2pdf/*.jpg
%{py_sitedir}/%{module}/tools/py2pdf/*.txt
%dir %{py_sitedir}/%{module}/tools/pythonpoint
%{py_sitedir}/%{module}/tools/pythonpoint/*.py[co]
%{py_sitedir}/%{module}/tools/pythonpoint/*.dtd
%dir %{py_sitedir}/%{module}/tools/pythonpoint/styles
%{py_sitedir}/%{module}/tools/pythonpoint/styles/*.py[co]
# to -demos subpackage ?
%dir %{py_sitedir}/%{module}/graphics/samples
%{py_sitedir}/%{module}/graphics/samples/*.py[co]
# *.py as %doc for education
%doc %{py_sitedir}/%{module}/graphics/samples/*.py
%{py_sitedir}/%{module}/tools/pythonpoint/demos
