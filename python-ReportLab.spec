%include	/usr/lib/rpm/macros.python
%define		module	ReportLab
Summary:	Python library for generating PDFs and graphics
Summary(pl):	Modu³y Pythona do generowania PDFów oraz grafik
Name:		python-%{module}
Version:	1.13
Release:	1
License:	distributable
Group:		Libraries/Python
Source0:	http://www.reportlab.com/ftp/ReportLab_1_11.tgz
URL:		http://www.reportlab.com/
BuildRequires:	python-devel >= 2.2
BuildRequires:	rpm-pythonprov
%requires_eq	python
Requires:	python-Imaging
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	%{module}

%description
A library written in python that lets you generate platform
independant PDFs and graphics.
- PDF generation: Uses Python, a clean OO language, layered
  architecture
- Graphics: provides primitive shapes, reusable widgets, sample
  collections including business chart and diagrams
- PythonPoint: A utility for generating PDF slides from a simple XML
  format

%description -l pl
Biblioteka napisana w pythonie pozwalaj±ca na generowanie niezale¿nych
od platformy PDF-ów oraz grafik.
- Generowanie PDF: U¿ywa Pythona, przejrzystego jêzyka obiektowego o
  warstwowej architekturze
- Grafika: podstawowe figury geometryczne, kontrolki, a tak¿e
  przyk³ady, w³±czaj±c w to wykresy i diagramy
- PythonPoing: Narzêdzie do generowania slajdów w formacie PDF z
  prostego formatu XML

%prep
%setup -q -n reportlab

%build
%{__make} -C lib -f Makefile.pre.in boot
%{__make} -C lib OPT="%{rpmcflags}" CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{py_sitedir}/%{module}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -rf test
cp -aR * $RPM_BUILD_ROOT%{py_sitedir}/%{module}
mv demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

echo "%{module}" > $RPM_BUILD_ROOT%{py_sitedir}/reportlab.pth
ln -s %{module} $RPM_BUILD_ROOT%{py_sitedir}/reportlab

install tools/py2pdf/py2pdf.py $RPM_BUILD_ROOT%{_bindir}
install tools/pythonpoint/pythonpoint.py $RPM_BUILD_ROOT%{_bindir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

gzip -9nf license.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* license*
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
%dir %{py_sitedir}/%{module}/tools/pythonpoint
%{py_sitedir}/%{module}/tools/pythonpoint/*.py[co]
%dir %{py_sitedir}/%{module}/tools/pythonpoint/styles
%{py_sitedir}/%{module}/tools/pythonpoint/styles/*.py[co]
