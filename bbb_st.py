import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

plt.rcParams.update({
    "text.usetex": True,
    "text.latex.preamble": r'\usepackage{amsmath}' # r""表示不转义""中的\
})

def C1lexi(n):
    fig = plt.figure(figsize=(1.2*n,0.8*n))
    plt.title(r"$C_{1}^{\le\xi}$ when $n=" + str(n) + "$")

    begin1 = r"$\begin{smallmatrix}"
    end1 = r"\end{smallmatrix}$"
    end2 = r"\end{smallmatrix}[-1]$"

    for j in range(0,n):
        middle = ""
        for i in range(j+1,0,-1): # (begin, end, step)
            middle += str(n-i+1)
            middle += " \\\\ "
        Aj = begin1 + middle + end2
        plt.text(j, j, Aj, ha = 'center', va = 'center')
        if j != 0:
            plt.annotate('', (j,j), (j-1,j-1), arrowprops=dict(arrowstyle = "->", shrinkA = 6, shrinkB = 9))
    
    for k in range(0,n):
        for j in range(0,n-k):
            middle = ""
            for i in range(j+1,0,-1):
                middle += str(n-i-k+1)
                middle += " \\\\ "
            Bkj = begin1 + middle + end1
            plt.text(2*(k+1)+j, j, Bkj, ha = 'center', va = 'center')
            if j != 0:
                plt.annotate('', (2*(k+1)+j,j), (2*(k+1)+j-1,j-1), arrowprops=dict(arrowstyle = "->", shrinkA = 6, shrinkB = 9))
            if j != n-1:
                plt.annotate('', (2*(k+1)+j,j), (2*(k+1)+j-1,j+1), arrowprops=dict(arrowstyle = "->", shrinkA = 6, shrinkB = 9))

    plt.xlim(0, 2*n)
    plt.ylim(0, n)
    plt.axis('off')
    # plt.show()
    return fig

begin = r"$\begin{pmatrix}"
end = r"\end{pmatrix}$"

def gM(n):
    fig = plt.figure(figsize=(1.5*n,n))
    plt.title("$g(M)$ when $n=" + str(n) + "$")

    new = np.zeros((n,n))
    for i in range(0,n):
        new[i,n-i-1] = 1

    for j in range (0,n):
        middle = ""
        for i in range(0,n):
            middle += str(int(new[j, i]))
            middle += " \\\\ "
        Aj = begin + middle + end
        plt.text(j, j, Aj, ha = 'center', va = 'center')
        if j != 0:
            plt.annotate('', (j,j), (j-1,j-1), arrowprops=dict(arrowstyle = "->", shrinkA = 12, shrinkB = 18))

    for k in range(0,n):
        old = new
        new = np.zeros((n,n))
        for j in range(0,n-k):
            middle = ""
            if j != 0:
                new[j,:] += new[j-1,:]
            if j != n-1:
                new[j,:] += old[j+1,:]
            new[j,:] -= old[j,:]
            for i in range(0,n):
                middle += str(int(new[j, i]))
                middle += " \\\\ "
            Bkj = begin + middle + end
            plt.text(2*(k+1)+j, j, Bkj, ha = 'center', va = 'center')
            if j != 0:
                plt.annotate('', (2*(k+1)+j,j), (2*(k+1)+j-1,j-1), arrowprops=dict(arrowstyle = "->", shrinkA = 12, shrinkB = 18))
            if j != n-1:
                plt.annotate('', (2*(k+1)+j,j), (2*(k+1)+j-1,j+1), arrowprops=dict(arrowstyle = "->", shrinkA = 12, shrinkB = 18))

    plt.xlim(0, 2*n)
    plt.ylim(0, n)
    plt.axis('off')
    # plt.show()
    return fig

def socFM(n):
    fig = plt.figure(figsize=(1.5*n,n))
    plt.title("$soc(FM)$ when $n=" + str(n) + "$")

    middle = ""
    for i in range(0,n):
        middle += "0 \\\\ "
    A = begin + middle + end
    for j in range(0,n):
        plt.text(j, j, A, ha = 'center', va = 'center')
        if j != 0:
            plt.annotate('', (j,j), (j-1,j-1), arrowprops=dict(arrowstyle = "->", shrinkA = 12, shrinkB = 18))

    new = np.zeros(n)
    for k in range(0,n):
        new[n-k-1] = 1
        middle = ""
        for i in range(0,n):
            middle += str(int(new[i]))
            middle += " \\\\ "
        Bk = begin + middle + end
        for j in range(0,n-k):
            plt.text(2*(k+1)+j, j, Bk, ha = 'center', va = 'center')
            if j != 0:
                plt.annotate('', (2*(k+1)+j,j), (2*(k+1)+j-1,j-1), arrowprops=dict(arrowstyle = "->", shrinkA = 12, shrinkB = 18))
            if j != n-1:
                plt.annotate('', (2*(k+1)+j,j), (2*(k+1)+j-1,j+1), arrowprops=dict(arrowstyle = "->", shrinkA = 12, shrinkB = 18))
        new[n-k-1] = 0

    plt.xlim(0, 2*n)
    plt.ylim(0, n)
    plt.axis('off')
    # plt.show()
    return fig

def convert(n, array, map):
    result = ""
    for i in range(0,2*n):
        if array[i] == -1:
            array[i+n] = 1 # 由于这里的修改不会影响本体，这个-1会被错误地继承下去，算是个bug，不过好在不影响结果
        elif array[i] == 1:
            result += "y_{" + str(int(map[0,i])) + "," + str(int(map[1,i])) + "}"
    return result

def Lm(n):
    fig = plt.figure(figsize=(1.2*n,0.8*n))
    plt.title("$L(m)$ when $n=" + str(n) + "$")

    begin1 = "$L("
    end1 = ")$"

    dynkin = np.zeros((1,n))
    for i in range(0,n):
        dynkin[0,i] = i+1
    xi = -1*dynkin + np.ones((1,n))

    dynkin = np.hstack((dynkin, dynkin))
    xi = np.hstack((xi, xi - 2*np.ones((1,n))))
    map = np.vstack((dynkin, xi))

    new = np.zeros((n,2*n))
    for i in range(0,n):
        new[i,n-i-1] = 1

    for j in range(0,n):
        Aj = begin1 + convert(n, new[j,:], map) + end1
        plt.text(j, j, Aj, ha = 'center', va = 'center')
        if j != 0:
            plt.annotate('', (j,j), (j-1,j-1), arrowprops=dict(arrowstyle = "->", shrinkA = 6, shrinkB = 9))
    
    for k in range(0,n):
        old = new
        new = np.zeros((n,2*n))
        for j in range(0,n-k):
            if j != 0:
                new[j,:] += new[j-1,:]
            if j != n-1:
                new[j,:] += old[j+1,:]
            new[j,:] -= old[j,:]
            Bkj = begin1 + convert(n, new[j,:], map) + end1
            plt.text(2*(k+1)+j, j, Bkj, ha = 'center', va = 'center')
            if j != 0:
                plt.annotate('', (2*(k+1)+j,j), (2*(k+1)+j-1,j-1), arrowprops=dict(arrowstyle = "->", shrinkA = 6, shrinkB = 9))
            if j != n-1:
                plt.annotate('', (2*(k+1)+j,j), (2*(k+1)+j-1,j+1), arrowprops=dict(arrowstyle = "->", shrinkA = 6, shrinkB = 9))

    plt.xlim(0, 2*n)
    plt.ylim(0, n)
    plt.axis('off')
    # plt.show()
    return fig

if 'nn' not in st.session_state: # Session State is a way to share variables between reruns, for each user session.
    st.session_state['nn'] = 0

st.title("Hi :D")
container = st.container()
col1, col2 = container.columns([0.75, 0.25])
with col1:
    nn = st.number_input("Type n here ⬇️", min_value=2, value=3) # n now
with col2:
    st.space("small")
    button = st.button("Confirm")
if button:
    st.session_state.nn = nn
col3, col4 = st.columns(2)
if 'nn' in st.session_state and st.session_state.nn > 1:
    n = st.session_state.nn
    with col3:
        st.pyplot(C1lexi(n))
        st.pyplot(socFM(n))
    with col4:
        st.pyplot(gM(n))
        st.pyplot(Lm(n))

# if __name__ == '__main__':
#     n = 8
#     C1lexi(n)
#     gM(n)
#     socFM(n)
#     Lm(n)