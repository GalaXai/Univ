# Libraries used
import numpy as np
import uklad
import potegowa
import wykresy


def rozklad_qr(matrix):
    # Gram-Schmidt Algorythm
    matrix = matrix.astype(float)
    n = matrix.shape[0]  # Number of rows in the matrix
    v = matrix.copy()
    q = matrix.copy()
    r = np.zeros([n, n])
    for j in range(0, n):
        for i in range(0, j):
            r[i, j] = q[:, i].T @ matrix[:, j]
            v[:, j] = v[:, j] - r[i, j] * q[:, i]
        r[j, j] = np.linalg.norm(v[:, j])  # Sets diagonal to norm of v(column) matrix
        q[:, j] = v[:, j] / r[j, j]  # Divide Column by
    return q, r


def iteruj_roznica(matrix, eps=2e-10):
    """
    Compute the eigenvalues of a matrix using the QR algorithm without shifts.

    Parameters:
        matrix (np.ndarray): The input matrix.
        eps (float): The tolerance level for checking convergence (default is 2e-10).

    Returns:
        tuple: A tuple of two elements: the eigenvalues and the number of iterations.
    """
    max_eigens = []
    it = 0
    n = matrix.shape[0]
    # Convert the matrix to upper Hessenberg form (lower triangular part is ignored)
    matrix = np.tri l(matrix, -1) + np.triu(matrix)
    # Initialize k (index of the sub-matrix to work on)
    k = n
    while k > 1:
        max_eigens.append(np.diagonal(matrix).max())
        # Check if the sub-matrix is almost upper triangular
        if abs(matrix[k - 1][k - 2]) <= 2 * eps * (abs(matrix[k - 2][k - 2]) + abs(matrix[k - 1][k - 1])):
            matrix[k - 1][k - 2] = 0
            k = k - 2
        elif abs(matrix[k - 1][k - 2]) <= 2 * eps * (abs(matrix[k - 1][k - 1]) + abs(matrix[k - 1][k - 1])):
            matrix[k - 1][k - 2] = 0
            k = k - 1
        else:
            # If the iteration count reaches the maximum, return an empty list
            if it >= 1000 * n:
                return [], []

            # Compute the QR decomposition of the sub-matrix
            q, r = rozklad_qr(matrix[:k, :k])
            # Rebuild the Hessenberg matrix using the QR decomposition
            matrix[:k, :k] = r @ q
            it = it + 1
    eigen_values = np.diagonal(matrix)
    return eigen_values, it, max_eigens


# Comparing methods
u1 = uklad.Uklad(10)
u1.losuj_uklad_symetryczny_dodatnio_okreslony()

q, r = rozklad_qr(u1.A)
eigen_values, iter_qr, list_eigens = iteruj_roznica(r @ q)

p1 = potegowa.Potegowa(u1)
iter_potegowa = p1.iteruj_roznica(eps=2e-10, wyswietlaj=0)
wykres = wykresy.Wykresy()

wykres.badaj_zbieznosc(
    tytul="Dominująca wartość własna",
    opis_OY="Lambda",
    dane1=p1.lambdy,
    opis1="Metoda Potęgowa",
    dane2=list_eigens,
    opis2="Metoda QR"

)
print(f"Ilosc iteracji\nMetoda potęgowa: {iter_potegowa},\nMetoda QR: {iter_qr}")

# Adidtional testing
list_iter = {
    "poteg": [],
    "qr": [],
}
for i in range(10):
    u1 = uklad.Uklad(10)
    u1.losuj_uklad_symetryczny_dodatnio_okreslony()

    q, r = rozklad_qr(u1.A)
    eigen_values, iter_qr, list_eigens = iteruj_roznica(r @ q)

    p1 = potegowa.Potegowa(u1)
    iter_potegowa = p1.iteruj_roznica(eps=2e-10, wyswietlaj=0)

    list_iter["poteg"].append(iter_potegowa)
    list_iter["qr"].append(iter_qr)

print(list_iter)
