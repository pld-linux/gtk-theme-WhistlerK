Summary:	WhistlerK - A Whistler-like gtk+ theme engine
Summary(pl):	Temat dla GTK bazuj±cy na Whistlerze
Name:		gtk-theme-WhistlerK
Version:	1.0.0
Release:	1
License:	GPL
Group:		Themes/Gtk
Source0:	http://download.classic.themes.org/gtk/WhistlerK-1.2.x.tar.gz
Patch0:		%{name}-configure.in.patch
URL:		http://www.themes.org/resources/236/
BuildRequires:	gtk+-devel >= 1.2.0
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
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
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
