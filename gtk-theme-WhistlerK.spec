Summary:	WhistlerK - A Whistler-like gtk+ theme engine
Summary(pl):	Temat dla GTK bazuj±cy na Whistlerze
Name:		gtk-theme-WhistlerK
Version:	0.1
Release:	1
License:	GPL
Group:		Themes/Gtk
Group(de):	Themen/Gtk
Group(pl):	Motywy/Gtk
Source0:	http://www.themes.org/resources/236/download/file.tgz
Patch0:		%{name}-configure.in.patch
URL:		http://www.themes.org/resources/236/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
A Whistler-like gtk+ theme engine.

%description -l pl
Temat dla GTK bazuj±cy na Whistlerze.

%prep
%setup  -q -n %{name}
%patch0 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk/themes/engines/*.so
%{_datadir}/themes/WhistlerK
