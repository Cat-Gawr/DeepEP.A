#ifndef MULTITHREADING_H
#define MULTITHREADING_H


//Simple portable thread library.

//Windows threads.
#if defined(WIN32) || defined(_WIN32) || defined(WIN64) || defined(_WIN64)
#include <windows.h>

typedef HANDLE CUTThread;
typedef unsigned(WINAPI *CUT_THREADROUTINE)(void *);

#define CUT_THREADPROC unsigned WINAPI
#define  CUT_THREADEND return 0

#else
//POSIX threads.
#include <pthread.h>

typedef pthread_t CUTThread;
typedef void *(*CUT_THREADROUTINE)(void *);

#define CUT_THREADPROC void
#define  CUT_THREADEND
#endif


#ifdef __cplusplus
extern "C" {
#endif

//Create thread.
CUTThread cutStartThread(CUT_THREADROUTINE, void *data);

//Wait for thread to finish.
void cutEndThread(CUTThread thread);

//Destroy thread.
void cutDestroyThread(CUTThread thread);

//Wait for multiple threads.
void cutWaitForThreads(const CUTThread *threads, int num);

#ifdef __cplusplus
} //extern "C"
#endif

#endif //MULTITHREADING_H
