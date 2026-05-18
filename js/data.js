// ── MOCK DATA (reemplazar con fetch() a la API Django) ──

const DB = {
  genres: [
    { id: 1, nombre: 'Literatura latinoamericana' },
    { id: 2, nombre: 'Clásicos universales' },
    { id: 3, nombre: 'Poesía' },
    { id: 4, nombre: 'Ciencia ficción' },
    { id: 5, nombre: 'Historia' },
    { id: 6, nombre: 'Filosofía' },
  ],

  authors: [
    { id: 1, nombre: 'Julio Cortázar',          nacionalidad: 'Argentina',        bio: 'Escritor y traductor argentino.' },
    { id: 2, nombre: 'Gabriel García Márquez',   nacionalidad: 'Colombia',         bio: 'Premio Nobel de Literatura 1982.' },
    { id: 3, nombre: 'Jorge Luis Borges',        nacionalidad: 'Argentina',        bio: 'Maestro del cuento fantástico.' },
    { id: 4, nombre: 'Franz Kafka',              nacionalidad: 'República Checa',  bio: 'Escritor esencial del siglo XX.' },
    { id: 5, nombre: 'Pablo Neruda',             nacionalidad: 'Chile',            bio: 'Premio Nobel de Literatura 1971.' },
    { id: 6, nombre: 'Juan Rulfo',               nacionalidad: 'México',           bio: 'Autor de Pedro Páramo.' },
  ],

  books: [
    { id: 1, titulo: 'Rayuela',                 autor_id: 1, genero_id: 1, anio: 1963, isbn: '978-84-376-0494-7', descripcion: 'Una novela experimental que puede leerse de múltiples formas.',           disponible: true,  portada: '📕', color: '#2a1c2a' },
    { id: 2, titulo: 'Cien años de soledad',    autor_id: 2, genero_id: 1, anio: 1967, isbn: '978-84-397-0124-6', descripcion: 'La saga de la familia Buendía en el mítico pueblo de Macondo.',           disponible: true,  portada: '📗', color: '#1a2e1a' },
    { id: 3, titulo: 'Ficciones',               autor_id: 3, genero_id: 2, anio: 1944, isbn: '978-84-663-0407-4', descripcion: 'Cuentos que exploran laberintos, espejos y mundos paralelos.',            disponible: false, portada: '📘', color: '#1c2a3a' },
    { id: 4, titulo: 'El proceso',              autor_id: 4, genero_id: 2, anio: 1925, isbn: '978-84-376-0209-7', descripcion: 'Josef K. despertó una mañana y fue arrestado sin razón aparente.',         disponible: true,  portada: '📙', color: '#3d2b1f' },
    { id: 5, titulo: 'Veinte poemas de amor',   autor_id: 5, genero_id: 3, anio: 1924, isbn: '978-84-376-0301-8', descripcion: 'El libro de poesía más leído en lengua española del siglo XX.',           disponible: true,  portada: '📓', color: '#2d1e30' },
    { id: 6, titulo: 'Pedro Páramo',            autor_id: 6, genero_id: 1, anio: 1955, isbn: '978-84-376-0512-8', descripcion: 'Juan Preciado viaja a Comala en busca de su padre Pedro Páramo.',         disponible: false, portada: '📒', color: '#1e3040' },
    { id: 7, titulo: 'El aleph',                autor_id: 3, genero_id: 4, anio: 1949, isbn: '978-84-663-1234-5', descripcion: 'Un punto en el espacio que contiene todos los demás puntos.',             disponible: true,  portada: '📕', color: '#2a2a1c' },
    { id: 8, titulo: 'La metamorfosis',         autor_id: 4, genero_id: 2, anio: 1915, isbn: '978-84-376-0887-2', descripcion: 'Gregor Samsa despertó convertido en un monstruoso insecto.',              disponible: true,  portada: '📗', color: '#1e2820' },
  ],

  users: [
    { id: 1, nombre: 'Luciana Mamani',   email: 'luciana@mail.com', password: '1234', role: 'admin' },
    { id: 2, nombre: 'Mariano Abizanda', email: 'mariano@mail.com', password: '1234', role: 'admin' },
    { id: 3, nombre: 'Ana García',       email: 'ana@mail.com',     password: '1234', role: 'user'  },
    { id: 4, nombre: 'Carlos López',     email: 'carlos@mail.com',  password: '1234', role: 'user'  },
  ],

  reservations: [
    { id: 1, user_id: 3, book_id: 3, fecha_reserva: '2025-05-01', fecha_devolucion: '2025-05-15', estado: 'activa'  },
    { id: 2, user_id: 3, book_id: 6, fecha_reserva: '2025-04-20', fecha_devolucion: '2025-05-05', estado: 'vencida' },
    { id: 3, user_id: 4, book_id: 1, fecha_reserva: '2025-05-10', fecha_devolucion: '2025-05-25', estado: 'activa'  },
  ],

  getBook:             (id) => DB.books.find(b => b.id === id),
  getAuthor:           (id) => DB.authors.find(a => a.id === id),
  getGenre:            (id) => DB.genres.find(g => g.id === id),
  getUser:             (id) => DB.users.find(u => u.id === id),
  getUserByEmail:      (email) => DB.users.find(u => u.email === email),
  getBookWithDetails:  (book) => ({ ...book, autor: DB.getAuthor(book.autor_id), genero: DB.getGenre(book.genero_id) }),
  getUserReservations: (user_id) =>
    DB.reservations
      .filter(r => r.user_id === user_id)
      .map(r => ({ ...r, libro: DB.getBookWithDetails(DB.getBook(r.book_id)) })),
};