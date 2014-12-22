Name:           unifdef
Version:        2.10
Release:        0
License:        BSD-2-Clause
Summary:        Removes ifdefs from C files
Url:            http://dotat.at/prog/unifdef/
Group:          Development/Tools
Source:         http://dotat.at/prog/unifdef/%{name}-%{version}.tar.gz
Source1001:     unifdef.manifest

%description
Unifdef is useful for removing ifdef'ed lines from a file while otherwise
leaving the file alone.  Unifdef acts on #ifdef, #ifndef, #else, and #en­
dif lines, and it knows only enough about C to know when one of these is
inactive because it is inside a comment, or a single or double quote.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%__make %{?_smp_mflags} CC=gcc CFLAGS="%{optflags}"

%install
make install DESTDIR=%{buildroot} prefix=%{_prefix}

%files
%manifest %{name}.manifest
%license COPYING
%{_bindir}/unifdef
%{_bindir}/unifdefall
%{_mandir}/man1/unifdef.1*
%{_mandir}/man1/unifdefall.1*
